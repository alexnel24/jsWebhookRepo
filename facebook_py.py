from facebook_business.adobjects.lead import Lead
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<LEAD_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
}
print Lead(id).get(
  fields=fields,
  params=params,
)