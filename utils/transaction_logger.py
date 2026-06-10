import time


def execute_transaction(
        logger,
        transaction_name,
        action):

    start_time = time.perf_counter()

    try:

        result = action()

        duration = round(
            time.perf_counter() - start_time,
            3
        )

        logger.log_result(
            transaction_name,
            "PASS",
            duration,
            None
        )

        return result

    except Exception as e:

        duration = round(
            time.perf_counter() - start_time,
            3
        )

        logger.log_result(
            transaction_name,
            "FAIL",
            duration,
            str(e)
        )

        raise