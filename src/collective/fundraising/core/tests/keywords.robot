*** Settings ***

Library  Selenium2Library  timeout=10  implicit_wait=0.5 
Library  OperatingSystem

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/variables.robot
Resource  plone/app/robotframework/keywords.robot


*** Keywords ***

Start browser
    Open browser  ${PLONE_URL}

Create dexterity type
    [Arguments]  ${title}  ${id}
    Go to  ${PLONE_URL}/@@dexterity-types
    Click Overlay Button  css=#add-type input
    Input Text  css=#formfield-form-widgets-title input  ${title}
    Input Text  css=#formfield-form-widgets-id input  ${id}
    Input Text  css=#formfield-form-widgets-description textarea  Test content type: ${title}
    Click Button  Add
    
    Wait until page contains element  link=Overview
    Click Overview in edit bar
    Select radiobutton  form.widgets.filter_content_types  all
    Click Button  Apply

Enable behavior 
    [Arguments]  ${name}
    Click Behaviors in edit bar
    ${for}=  Get element attribute  xpath=//label[contains(., "${name}")]@for
    Select checkbox  id=${for}

    Click button  Save
    Page should contain  Behaviors successfully updated
    Checkbox should be selected  id=${for}

Populate Fundraising Settings field
    [Arguments]  ${name}  ${value}
    Input text  form-widgets-IFundraisingSettings-${name}  ${value}

Select Fundraising Settings checkbox
    [Arguments]  ${name}
    Select checkbox  form-widgets-IFundraisingSettings-${name}-0

Fundraising Settings value should be
    [Arguments]  ${name}  ${value}
    Textfield value should be  form-widgets-IFundraisingSettings-${name}  ${value}

Fundraising Settings checkbox should be selected
    [Arguments]  ${name}
    Checkbox should be selected  form-widgets-IFundraisingSettings-${name}-0

Populate Fundraising Campaign field
    [Arguments]  ${name}  ${value}
    Input text  form-widgets-IFundraisingCampaign-${name}  ${value}

Select Fundraising Campaign checkbox
    [Arguments]  ${name}
    Select checkbox  form-widgets-IFundraisingCampaign-${name}-0

Fundraising Campaign value should be
    [Arguments]  ${name}  ${value}
    Textfield value should be  form-widgets-IFundraisingCampaign-${name}  ${value}

Fundraising Campaign checkbox should be selected
    [Arguments]  ${name}
    Checkbox should be selected  form-widgets-IFundraisingCampaign-${name}-0

Populate Fundraising Page field
    [Arguments]  ${name}  ${value}
    Input text  form-widgets-IFundraisingPage-${name}  ${value}

Fundraising Page value should be
    [Arguments]  ${name}  ${value}
    Textfield value should be  form-widgets-IFundraisingPage-${name}  ${value}

Populate Personal Fundraiser field
    [Arguments]  ${name}  ${value}
    Input text  form-widgets-IPersonalFundraiser-${name}  ${value}

Personal Fundraiser value should be
    [Arguments]  ${name}  ${value}
    Textfield value should be  form-widgets-IPersonalFundraiser-${name}  ${value}

Populate Donor field
    [Arguments]  ${name}  ${value}
    Input text  form-widgets-IDonor-${name}  ${value}

Donor value should be
    [Arguments]  ${name}  ${value}
    Textfield value should be  form-widgets-IDonor-${name}  ${value}

Populate Donation field
    [Arguments]  ${name}  ${value}
    Input text  form-widgets-IDonation-${name}  ${value}

Donation value should be
    [Arguments]  ${name}  ${value}
    Textfield value should be  form-widgets-IDonation-${name}  ${value}
