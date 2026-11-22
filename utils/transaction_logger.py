import time
import inspect
from pathlib import Path
import os

# Keep stored error text within your MySQL column. Selenium/Appium messages can be
# very long (full stack traces). Adjust to match the actual column size.
MAX_ERROR_LEN = 1000


def get_run_type() -> str:
    """Detects if the script is running inside Jenkins or locally."""
    jenkins_env_vars = ["JENKINS_URL", "BUILD_NUMBER", "JENKINS_HOME"]
    if any(var in os.environ for var in jenkins_env_vars):
        return "Jenkins"
    return "Local"


def _safe_log(logger, **kwargs):
    """Log a result without ever letting a logging problem (DB down, column too
    short, etc.) replace the real test outcome."""
    try:
        logger.log_result(**kwargs)
    except Exception as log_err:
        print(f"WARNING: could not log {kwargs.get('status')} for "
              f"{kwargs.get('test_name')}: {log_err}")


def execute_transaction(
        logger,
        transaction_name,
        action,
        test_script=None,
        run_type=None):

    # ---------------------------------------------------------
    # Automatically determine the pytest script filename
    # if it was not explicitly provided.
    # ---------------------------------------------------------
    if test_script is None:
        frame = inspect.currentframe()

        try:
            caller_frame = frame.f_back

            if caller_frame is not None:
                caller_file = caller_frame.f_code.co_filename
                test_script = Path(caller_file).name
            else:
                test_script = "Unknown"
        finally:
            del frame

    # Determine execution environment unless the caller supplied one
    if run_type is None:
        run_type = get_run_type()

    start_time = time.perf_counter()

    try:
        result = action()

    except Exception as e:
        duration = round(time.perf_counter() - start_time, 3)

        _safe_log(
            logger,
            test_name=transaction_name,
            status="FAIL",
            duration=duration,
            error_message=(str(e) or type(e).__name__)[:MAX_ERROR_LEN],
            test_script=test_script,
            run_type=run_type,
        )

        # Always re-raise: a failed transaction must stop the test so later steps
        # do not run against the wrong screen.
        raise

    duration = round(time.perf_counter() - start_time, 3)

    _safe_log(
        logger,
        test_name=transaction_name,
        status="PASS",
        duration=duration,
        error_message=None,
        test_script=test_script,
        run_type=run_type,
    )

    return result