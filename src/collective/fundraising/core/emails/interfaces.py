from zope import schema
from zope.interface import Interface
from plone.directives import form

class IBaseCampaignPageData(Interface):
    campaign_name = schema.TextLine(
        title=u"Campaign Name",
        description=u"The name of the Fundraising Campaign",
    )
    campaign_url = schema.TextLine(
        title=u"Campaign URL",
        description=u"The URL of the Fundraising Campaign",
    )
    campaign_image_url = schema.TextLine(
        title=u"Campaign Image URL",
        description=u"The URL of the full sized main image for the campaign, if provided",
        required=False,
    )
    campaign_header_image_url = schema.TextLine(
        title=u"Campaign Header Image URL",
        description=u"The URL of the full sized custom header image for the campaign, if provided",
        required=False,
    )
    campaign_goal = schema.Int(
        title=u"Campaign Goal",
        description=u"The goal for the campaign",
    )
    campaign_raised = schema.Int(
        title=u"Campaign Raised",
        description=u"The amount raised thus far by the campaign",
    )
    campaign_percent = schema.Int(
        title=u"Campaign Percent",
        description=u"The percentage of goal completion by the campaign",
    )
    page_name = schema.TextLine(
        title=u"Page Name",
        description=u"If this donation was to a personal campaign page, the name of the page",
    )
    fundraiser_first = schema.TextLine(
        title=u"Page Fundraiser First Name",
        description=u"The first name of the creator of this fundraiser",
    )
    fundraiser_last = schema.TextLine(
        title=u"Page Fundraiser Last Name",
        description=u"The last name of the creator of this fundraiser",
    )
    page_url = schema.TextLine(
        title=u"Page URL",
        description=u"If this donation was to a personal campaign page, the url of the page",
    )
    page_image_url = schema.TextLine(
        title=u"Page Image URL",
        description=u"If this donation was to a personal campaign page, the url to the full size image for the pagej",
    )
    page_goal = schema.Int(
        title=u"Page Goal",
        description=u"If this donation was to a personal campaign page, the goal for the page",
    )
    page_raised = schema.Int(
        title=u"Page Raised",
        description=u"If this donation was to a personal campaign page, the amount raised thus far by the page",
    )
    page_percent = schema.Int(
        title=u"Page Percent",
        description=u"If this donation was to a personal campaign page, the percentage of goal completion by the page",
    )

class IDedicationData(Interface):
    dedication_type = schema.TextLine(
        title=u"Dedication Type",
        description=u"The type of dedication such as memorial or honorary",
    )
    first_name = schema.TextLine(
        title=u"Donor's First Name",
        description=u"The first name of the donor",
    )
    last_name = schema.TextLine(
        title=u"Donor's Last Name",
        description=u"The last name of the donor",
    )
    dedication_first_name = schema.TextLine(
        title=u"Dedicated To: First Name",
        description=u"The first name of the honoree",
    )
    dedication_last_name = schema.TextLine(
        title=u"Dedicated To: Last Name",
        description=u"The last name of the honoree",
    )
    recipient_first_name = schema.TextLine(
        title=u"Recipient First Name",
        description=u"The first name of the recipient",
    )
    recipient_last_name = schema.TextLine(
        title=u"Recipient Last Name",
        description=u"The last name of the recipient",
    )
    amount = schema.Int(
        title=u"Amount",
        description=u"The amount of the donation",
    )
    block_message = schema.TextLine(
        title=u"Message",
        description=u"The message in html format.",
    )

class IThankYouData(form.Schema, IBaseCampaignPageData):
    block_receipt = schema.Text(
        title=u"Receipt HTML",
        description=u"The HTML code for the receipt itself",
    )
    block_campaign_thank_you = schema.Text(
        title=u"Campaign Thank You HTML",
        description=u"The campaign's custom thank you message",
    )
    amount = schema.Int(
        title=u"Amount",
        description=u"The amount of the donation",
    )
    first_name = schema.TextLine(
        title=u"First Name",
        description=u"The first name of the donor",
    )
    last_name = schema.TextLine(
        title=u"Last Name",
        description=u"The last name of the donor",
    )

class IPersonalFundraiserCreatedData(form.Schema, IBaseCampaignPageData):
    """ Schema for emails thanking fundraiser for creating a personal campaign page """

class IPersonalFundraiserDonationData(form.Schema, IBaseCampaignPageData):
    amount = schema.Int(
        title=u"Amount",
        description=u"The amount of the donation",
    )
    first_name = schema.TextLine(
        title=u"Donor First Name",
        description=u"The first name of the donor",
    )
    last_name = schema.TextLine(
        title=u"Donor Last Name",
        description=u"The last name of the donor",
    )
    donor_email = schema.TextLine(
        title=u"The Donor's email address",
        description=u"The last name of the donor",
    )
