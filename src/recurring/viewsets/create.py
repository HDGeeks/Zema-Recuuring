import time
from rest_framework.viewsets import ModelViewSet
from recurring.models import DirectDebitMandate
from recurring.serializers import DirectDebitMandateSerializer
from rest_framework import request
import requests
import environ
from rest_framework.response import Response

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


class CreateDebitMandateViewSet(ModelViewSet):
    queryset = DirectDebitMandate.objects.all()
    serializer_class = DirectDebitMandateSerializer

    def create(self, request, *args, **kwargs):
        # Retrieve data from request
        payee_identifier_type = request.data.get("payee_identifier_type")
        payee_identifier_value = request.data.get("payee_identifier_value")
        payer_reference_number = request.data.get("payer_reference_number")
        agreed_tc = request.data.get("agreed_tc")
        payee_account_name = request.data.get("payee_account_name")
        payer_account_name = request.data.get("payer_account_name")
        first_payment_date = request.data.get("first_payment_date")
        frequency = request.data.get("frequency")
        start_range_of_days = request.data.get("start_range_of_days")
        end_range_of_days = request.data.get("end_range_of_days")
        expiry_date = request.data.get("expiry_date")

        # Use helper function to modify XML
        xml = create_direct_debit_mandate_xml(
            payee_identifier_type,
            payee_identifier_value,
            payer_reference_number,
            agreed_tc,
            payee_account_name,
            payer_account_name,
            first_payment_date,
            frequency,
            start_range_of_days,
            end_range_of_days,
            expiry_date,
        )

        # Send XML as request
        response = requests.post(env("url"), data=xml)

        return Response(response)


def create_direct_debit_mandate_xml(
    payee_identifier_type,
    payee_identifier_value,
    payer_reference_number,
    agreed_tc,
    payee_account_name,
    payer_account_name,
    first_payment_date,
    frequency,
    start_range_of_days,
    end_range_of_days,
    expiry_date,
):
    xml = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:api="http://cps.huawei.com/cpsinterface/api_requestmgr" xmlns:req="http://cps.huawei.com/cpsinterface/request" xmlns:com="http://cps.huawei.com/cpsinterface/common">
  <soapenv:Header/>
  <soapenv:Body>
    <api:Request>
      <req:Header>
        <req:Version>1.0</req:Version>
        <req:CommandID>CreateDirectDebitMandateByCustomer</req:CommandID>
        <req:OriginatorConversationID>S_X2013012921001</req:OriginatorConversationID>
        <req:ConversationID>AG_20130129T102103</req:ConversationID>
        <req:Caller>
          <req:CallerType>2</req:CallerType>
          <req:ThirdPartyID>{env('IdentifierType14')}</req:ThirdPartyID>
          <req:Password>{env('password')}</req:Password>
          <req:ResultURL>http://10.71.109.150:8888/mockResultBinding</req:ResultURL>
        </req:Caller>
        <req:KeyOwner>1</req:KeyOwner>
        <req:Timestamp>{createTimeStamp()}</req:Timestamp>
      </req:Header>
      <req:Body>
        <req:Identity>
          <req:Initiator>
            <req:IdentifierType>14</req:IdentifierType>
            <req:Identifier>{env('IdentifierType14')}</req:Identifier>
            <req:SecurityCredential>{env('SecurityCredential14')}</req:SecurityCredential>
          </req:Initiator>
          <req:ReceiverParty>
            <req:IdentifierType>1</req:IdentifierType>
            <req:Identifier>{env('IdentifierType11')}</req:Identifier>
          </req:ReceiverParty>
        </req:Identity>
        <req:CreateDirectDebitMandateByPayerRequest>
          <req:Payee>
            <com:IdentifierType>{payee_identifier_type}</com:IdentifierType>
            <com:IdentifierValue>{payee_identifier_value}</com:IdentifierValue>
          </req:Payee>
          <req:DirectDebitMandateInfo>
            <com:PayerReferenceNumber>{payer_reference_number}</com:PayerReferenceNumber>
            <com:AgreedTC>{agreed_tc}</com:AgreedTC>
            <com:PayeeAccountName>{payee_account_name}</com:PayeeAccountName>
            <com:PayerAccountName>{payer_account_name}</com:PayerAccountName>
            <com:FirstPaymentDate>{first_payment_date}</com:FirstPaymentDate>
            <com:Frequency>{frequency}</com:Frequency>
            <com:StartRangeOfDays>{start_range_of_days}</com:StartRangeOfDays>
            <com:EndRangeOfDays>{end_range_of_days}</com:EndRangeOfDays>
            <com:ExpiryDate>{expiry_date}</com:ExpiryDate>
          </req:DirectDebitMandateInfo>
        </req:CreateDirectDebitMandateByPayerRequest>
      </req:Body>
    </api:Request>
  </soapenv:Body>
</soapenv:Envelope>"""

    return xml


def createTimeStamp():
    return str(int(time.time()))
