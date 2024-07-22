from datetime import datetime

from aioyoomoney.methods import *


class Client:
    def __init__(self, token: str):
        self.token = token

    async def account_info(self):
        async with AccountMethod(self.token) as account:
            return account

    # def operation_history(self,
    #                       type: str = None,
    #                       label: str = None,
    #                       from_date: datetime = None,
    #                       till_date: datetime = None,
    #                       start_record: str = None,
    #                       records: int = None,
    #                       details: bool = None,
    #                       ):
    #     method = "operation-history"
    #     return History(base_url=self.base_url,
    #                    token=self.token,
    #                    method=method,
    #                    type=type,
    #                    label=label,
    #                    from_date=from_date,
    #                    till_date=till_date,
    #                    start_record=start_record,
    #                    records=records,
    #                    details=details,
    #                    )
    #
    # def operation_details(self, operation_id: str):
    #     method = "operation-details"
    #     return OperationDetails(base_url=self.base_url,
    #                             token=self.token,
    #                             method=method,
    #                             operation_id=operation_id,
    #                             )