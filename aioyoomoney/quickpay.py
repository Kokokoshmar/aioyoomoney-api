from .base import ContextSession


class Quickpay(ContextSession):
    def __init__(
        self,
        receiver: str,
        quickpay_form: str,
        targets: str,
        payment_type: str,
        sum: float,
        form_comment: str = None,
        short_dest: str = None,
        label: str = None,
        comment: str = None,
        success_url: str = None,
        need_fio: bool = False,
        need_email: bool = False,
        need_phone: bool = False,
        need_address: bool = False
    ):
        self.base_url = "https://yoomoney.ru/quickpay/confirm.xml?"

        payload = {
            "receiver": receiver,
            "quickpay_form": quickpay_form,
            "targets": targets,
            "paymentType": payment_type,
            "sum": sum,
            "formcomment": form_comment,
            "short_dest": short_dest,
            "label": label,
            "comment": comment,
            "successURL": success_url,
            "need_fio": need_fio,
            "need_email": need_email,
            "need_phone": need_phone,
            "need_address": need_address
        }

        self.payload = {k: v for k, v in payload.items() if v is not None}

        for value in self.payload:
            self.base_url += str(value).replace("_", "-") + "=" + str(payload[value])
            self.base_url += "&"

        self.base_url = self.base_url[:-1].replace(" ", "%20")
        self.redirected_url = None

        super().__init__(self.base_url, "POST")

    async def __aenter__(self):
        response = await super().__aenter__()
        self.redirected_url = response.url

        return self
