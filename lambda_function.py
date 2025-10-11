"""AWS Lambda function that says Hello World to SNS on schedule.

INPUT: EventBridge scheduled event
OUTPUT: send Hello World to SNS in chatbot format
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

from aws_lambda_powertools.logging import Logger

if TYPE_CHECKING:
    from aws_lambda_powertools.utilities.data_classes import EventBridgeEvent
    from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(service="lambda-sns")


def lambda_handler(_: EventBridgeEvent, __: LambdaContext) -> json:
    """Say Hello World."""
    context = {"message": "Hello World"}
    logger.info("CloudWatch logs group: %s", context.get("message"))

    # return the calculated area as a JSON string
    length = 10
    width = 10
    return json.dumps(calculate_area(length, width))


def calculate_area(length: int, width: int) -> int:
    """Elementary math."""
    return length * width
