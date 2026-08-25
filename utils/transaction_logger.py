import time
import inspect
from pathlib import Path


def execute_transaction(
        logger,
        transaction_name,
        action,
        test_script=None):

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

    start_time = time.perf_counter()

    try:

        result = action()

        duration = round(
            time.perf_counter() - start_time,
            3
        )

        logger.log_result(
            test_name=transaction_name,
            status="PASS",
            duration=duration,
            error_message=None,
            test_script=test_script
        )

        return result

    except Exception as e:

        duration = round(
            time.perf_counter() - start_time,
            3
        )

        logger.log_result(
            test_name=transaction_name,
            status="FAIL",
            duration=duration,
            error_message=str(e),
            test_script=test_script
        )

        raise