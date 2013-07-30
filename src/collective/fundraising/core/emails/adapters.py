from five import grok
from collective.fundraising.core.emails.interfaces import IThankYouData
from collective.fundraising.core.emails.interfaces import IDedicationData
from collective.fundraising.core.emails.interfaces import IPersonalFundraiserCreatedData
from collective.fundraising.core.emails.interfaces import IPersonalFundraiserDonationData
from collective.fundraising.core.behaviors.interfaces import IDonation
from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser


class DonationMappings(object):
    @property
    def donation(self):
        # NOTE: context here is the behavior instance, not the content type itself
        return self.context

    @property
    def donor(self):
        if self.donation is not None:
            return self.donation.get_donor()
    
    @property
    def page(self):
        if self.donation is not None:
            return self.donation.get_fundraising_page()

    @property
    def campaign(self):
        if self.page is not None:
            return self.page.get_fundraising_campaign()

    @property
    def personal_fundraiser(self):
        if self.page is not None:
            return self.page.get_personal_fundraiser()

    @property
    def campaign_name(self):
        if self.campaign is not None:
            return self.campaign.context.title
        
    @property
    def campaign_url(self):
        if self.campaign is not None:
            return self.campaign.context.absolute_url()
        
    @property
    def campaign_image_url(self):
        if self.campaign is not None:
            return self.campaign_url + '/@@images/image'
       
    @property
    def campaign_header_image_url(self):
        if self.campaign is not None:
            return self.campaign_url + '/@@images/header_image'

    @property
    def campaign_goal(self):
        if self.campaign is not None:
            return self.campaign.goal

    @property
    def campaign_raised(self):
        if self.campaign is not None:
            return self.campaign.total

    @property
    def campaign_percent(self):
        if self.campaign is not None:
            return self.campaign.get_goal_percent()

    @property
    def page_name(self):
        if self.page is not None:
            return self.page.context.title

    @property
    def page_url(self):
        if self.page is not None:
            return self.page.context.absolute_url()

    @property
    def page_image_url(self):
        if self.page is not None:
            return self.page_url + '/@@images/image'

    @property
    def page_goal(self):
        if self.page is not None:
            return self.page.goal

    @property
    def page_raised(self):
        if self.page is not None:
            return self.page.total

    @property
    def page_percent(self):
        if self.page is not None:
            return self.page.get_goal_percent()

    @property
    def amount(self):
        if self.donation is not None:
            return self.donation.amount

    @property
    def first_name(self):
        if self.donor is not None:
            return self.donor.first_name

    @property
    def last_name(self):
        if self.donor is not None:
            return self.donor.last_name

    @property
    def fundraiser_first(self):
        if self.page is not None:
            return self.personal_fundraiser.first_name

    @property
    def fundraiser_last(self):
        if self.personal_fundraiser is not None:
            return self.personal_fundraiser.last_name

class PersonalFundraiserMappings(DonationMappings): 
    """ Use mappings but assume context provides the IPersonalFundraiser 
        behavior rather than IDonation.  This is used for sending emails
        post-creation of of a personal fundraiser.
    """
    @property
    def donation(self):
        return None

    @property
    def personal_fundraiser(self):
        # NOTE: context here is the behavior instance, not the content type itself
        return self.context

    @property
    def page(self):
        if self.personal_fundraiser is not None:
            return self.personal_fundraiser.get_fundraising_page()

    @property
    def campaign(self):
        if self.personal_fundraiser is not None:
            return self.personal_fundraiser.get_fundraising_campaign()

class DedicationMappings(grok.Adapter, DonationMappings):
    grok.provides(IDedicationData)
    grok.context(IDonation)

    @property
    def dedication(self):
        if self.donation:
            return self.donation.get_dedication()

    @property
    def dedication_type(self):
        if self.dedication is not None:
            return self.dedication.dedication_type

    @property
    def dedication_first_name(self):
        if self.dedication is not None:
            return self.dedication.first_name

    @property
    def dedication_last_name(self):
        if self.dedication is not None:
            return self.dedication.last_name

    @property
    def recipient_first_name(self):
        if self.dedication is not None:
            return self.dedication.recipient_first_name

    @property
    def recipient_last_name(self):
        if self.dedication is not None:
            return self.dedication.recipient_last_name

    @property
    def block_message(self):
        if self.dedication:
            message = self.dedication.message
            if message is not None:
                return message.output

class ThankYouData(grok.Adapter, DonationMappings):
    grok.provides(IThankYouData)
    grok.context(IDonation)

    @property
    def block_receipt(self):
        if self.donation is not None:
            return self.donation.render_receipt()

    @property
    def block_thank_you(self):
        if self.personal_fundraiser is not None:
            return self.personal_fundraiser.thank_you
        if self.page is not None:
            return self.page.thank_you

class PersonalFundraiserDonationData(grok.Adapter, DonationMappings):
    grok.provides(IPersonalFundraiserDonationData)
    grok.context(IDonation)

    @property
    def amount(self):
        if self.donation is not None:
            return self.donation.amount

    @property
    def donor_email(self):
        if self.donor is not None:
            return self.donor.email

class PersonalFundraiserCreatedData(grok.Adapter, PersonalFundraiserMappings):
    grok.provides(IPersonalFundraiserCreatedData)
    grok.context(IPersonalFundraiser)

