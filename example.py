from __future__ import print_function
import sightseeingtech_passhub_api
from sightseeingtech_passhub_api import ApiClient, Configuration
from sightseeingtech_passhub_api.rest import ApiException


configuration = Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
configuration.host = 'YOUR_HOST'
configuration.verify_ssl = False

client = ApiClient(configuration)

try:
    productResourceApi = sightseeingtech_passhub_api.ProductResourceApi(client)

    print('Loading products...')

    products = productResourceApi.get_all_products()

    print('Product %d products is/are loaded.\n' % len(products))
except ApiException as e:
    print("Exception when calling ProductResourceApi->get_all_products: %s\n" % e)


try:
    orderResourceApi = sightseeingtech_passhub_api.OrderRecordResourceApi(client)

    print('Create order...')
    orderItem = sightseeingtech_passhub_api.OrderItem()
    orderItem.sku = '1GL5_Child'
    orderItem.quantity = 1
    orderItem.price_paid = 100
    orderItem.tour_date = '2019-01-01T00:00:00.000Z'
    orderItem.validation_id = 'validation id'
    orderItem.vendor_voucher_id = 'vendor voucher id'
    orderItem.group_name = 'groupName'
    orderItem.customer_name = 'Python API client'
    orderItem.customer_email = 'test@mail.com'
    orderItem.customer_company = 'company'

    group = sightseeingtech_passhub_api.GroupEntryDTO("groupName", [orderItem])

    orderRecord = sightseeingtech_passhub_api.OrderRecordDTO()
    orderRecord.amount = 10
    orderRecord.delivery_method = 'DIGITAL'
    orderRecord.groups = [group]
    orderRecord.originiator = 'originator'
    orderRecord.originator_order_id = 'originator order id'

    order = orderResourceApi.create_order_record(orderRecord)
    print("The order is created, with the order id: %d.\n" % order.id)

    print('Validate voucher...')
    voucherResourceApi = sightseeingtech_passhub_api.VoucherResourceApi(client)

    validationResult = voucherResourceApi.validate_voucher(order.groups[0].items[0].voucher_id, 12609)

    if validationResult.status == 'SUCCESS':
        print('The voucher is validated.\n')
    else:
        print('Voucher does not validated, validation status: %s.\n', validationResult.status)
except ApiException as e:
    print("Exception when creating order: %s\n" % e)
