*** Settings ***

Library  Selenium2Library  timeout=10  implicit_wait=0.5 
Library  OperatingSystem

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/variables.robot
Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/server.robot

Suite Setup  Start browser
Suite Teardown  Close All Browsers

*** Test Cases ***

Fundraising Settings fields store values
    [tags]  Fundraising Settings
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Fundraising Settings  test_fundraising_settings
    Enable behavior  Fundraising Settings

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Fundraising Settings")]/..
    Wait until page contains  Add Test Fundraising Settings

    Input text  form-widgets-IDublinCore-title  Test Organization Settings
    Populate Fundraising Settings field  org_name  Test Organization
    Populate Fundraising Settings field  ask_levels  5|5,10,25,50
    Populate Fundraising Settings field  ask_level  5
    Populate Fundraising Settings field  goal  100
    Populate Fundraising Settings field  ask_quantities  1|1,2,3,4,5
    Populate Fundraising Settings field  ask_quantity  1
    Select Fundraising Settings checkbox  allow_pf
    Populate Fundraising Settings field  completion_threshold  25
    Populate Fundraising Settings field  pf_completion_threshold  10
    Click Button  Save

    Click Edit in edit bar
    Fundraising Settings value should be  org_name  Test Organization
#    Fundraising Settings value should be  ask_levels  5|5,10,25,50
    Fundraising Settings value should be  ask_level  5
    Fundraising Settings value should be  goal  100
#    Fundraising Settings value should be  ask_quantities  1|1,2,3,4,5
    Fundraising Settings value should be  ask_quantity  1
    Fundraising Settings checkbox should be selected  allow_pf
    Fundraising Settings value should be  completion_threshold  25
    Fundraising Settings value should be  pf_completion_threshold  10
    
    Populate Fundraising Settings field  completion_threshold  15
    Populate Fundraising Settings field  pf_completion_threshold  5
    Click Button  Save

    Click Edit in edit bar
    Fundraising Settings value should be  completion_threshold  15
    Fundraising Settings value should be  pf_completion_threshold  5

Fundraising Campaign fields store values
    [tags]  Fundraising Campaign

    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Fundraising Campaign  test_fundraising_campaign
    Enable behavior  Fundraising Campaign

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Fundraising Campaign")]/..
    Wait until page contains  Add Test Fundraising Campaign

    Input text  form-widgets-IDublinCore-title  Test Fundraising Campaign
    Populate Fundraising Campaign field  goal  110
    Select Fundraising Campaign checkbox  allow_pf
    Click Button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  110
    Fundraising Campaign checkbox should be selected  allow_pf
    Populate Fundraising Campaign field  goal  210
    Click Button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  210
    Click Button  Save

Fundraising Page field store values
    [tags]  Fundraising Page

    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Fundraising Page  test_fundraising_page
    Enable behavior  Fundraising Page

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Fundraising Page")]/..
    Wait until page contains  Add Test Fundraising Page

    Input text  form-widgets-IDublinCore-title  Test Fundraising Page
    Populate Fundraising Page field  goal  120
    Click Button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  120
    Populate Fundraising Page field  goal  220
    Click Button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  220

Personal Fundraiser field stores values
    [tags]  Personal Fundraiser

    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Personal Fundraiser  test_fundraising_page
    Enable behavior  Personal Fundraiser

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Personal Fundraiser")]/..
    Wait until page contains  Add Test Personal Fundraiser

    Input text  form-widgets-IDublinCore-title  Test Personal Fundraiser
    Populate Personal Fundraiser field  pf_goal  130
    Click Button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  130
    Populate Personal Fundraiser field  pf_goal  230
    Click Button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  230

Personal Fundraiser can combine with page, campaign, and settings
    [tags]  Personal Fundraiser  Fundraising Page  Fundraising Campaign  Fundraising Settings
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Combo  test_combo
    Enable behavior  Fundraising Settings
    Enable behavior  Fundraising Campaign
    Enable behavior  Fundraising Page
    Enable behavior  Personal Fundraiser

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Combo")]/..
    Wait until page contains  Add Test Combo

    Input text  form-widgets-IDublinCore-title  Test Combo 

    Populate Fundraising Settings field  org_name  Test Organization
    Populate Fundraising Settings field  ask_levels  5|5,10,25,50
    Populate Fundraising Settings field  ask_level  5
    Populate Fundraising Settings field  goal  100
    Populate Fundraising Settings field  ask_quantities  1|1,2,3,4,5
    Populate Fundraising Settings field  ask_quantity  1
    Select Fundraising Settings checkbox  allow_pf
    Populate Fundraising Settings field  completion_threshold  25
    Populate Fundraising Settings field  pf_completion_threshold  10
    Populate Fundraising Campaign field  goal  110
    Select Fundraising Campaign checkbox  allow_pf
    Populate Fundraising Page field  goal  120
    Populate Personal Fundraiser field  pf_goal  130
    Click Button  Save

    Click Edit in edit bar
    Fundraising Settings value should be  org_name  Test Organization
#    Fundraising Settings value should be  ask_levels  5|5,10,25,50
    Fundraising Settings value should be  ask_level  5
    Fundraising Settings value should be  goal  100
#    Fundraising Settings value should be  ask_quantities  1|1,2,3,4,5
    Fundraising Settings value should be  ask_quantity  1
    Fundraising Settings checkbox should be selected  allow_pf
    Fundraising Settings value should be  completion_threshold  25
    Fundraising Settings value should be  pf_completion_threshold  10
    Fundraising Campaign value should be  goal  110
    Fundraising Campaign checkbox should be selected  allow_pf
    Fundraising Page value should be  goal  120
    Personal Fundraiser value should be  pf_goal  130

    Populate Fundraising Settings field  goal  200
    Populate Fundraising Campaign field  goal  210
    Populate Fundraising Page field  goal  220
    Populate Personal Fundraiser field  pf_goal  230
    Click Button  Save

    Click Edit in edit bar
    Fundraising Settings value should be  goal  200
    Fundraising Campaign value should be  goal  210
    Fundraising Page value should be  goal  220
    Personal Fundraiser value should be  pf_goal  230


Fundraising Campaign inherits default values from Fundraising Settings
    [tags]  Inheritance  Fundraising Campaign  Fundraising Settings
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Settings  test_settings
    Enable behavior  Fundraising Settings
    Create dexterity type  Test Campaign  test_campaign
    Enable behavior  Fundraising Campaign

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Settings")]/..
    Wait until page contains  Add Test Settings

    Input text  form-widgets-IDublinCore-title  Test Settings 
    Populate Fundraising Settings field  org_name  Test Organization
    Populate Fundraising Settings field  goal  100
    Select Fundraising Settings checkbox  allow_pf
    Click Button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Campaign")]/..
    Input text  form-widgets-IDublinCore-title  Test Campaign
    Click Button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  100
    Click Button  Cancel

    Go to  ${PLONE_URL}/test-settings
    Click Edit in edit bar
    Fundraising Settings value should be  goal  100
    Populate Fundraising Settings field  goal  200
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign
    Click Edit in edit bar
    Fundraising Campaign value should be  goal  200
    Populate Fundraising Campaign field  goal  300
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings
    Click Edit in edit bar
    Populate Fundraising Settings field  goal  400
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign
    Click Edit in edit bar
    Fundraising Campaign value should be  goal  300
    Click Button  Cancel
    

Fundraising Page inherits default values from Fundraising Campaign and Fundraising Settings
    [tags]  Inheritance  Fundraising Campaign  Fundraising Settings
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Settings  test_settings
    Enable behavior  Fundraising Settings
    Create dexterity type  Test Campaign  test_campaign
    Enable behavior  Fundraising Campaign

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Settings")]/..
    Wait until page contains  Add Test Settings

    Input text  form-widgets-IDublinCore-title  Test Settings 
    Populate Fundraising Settings field  org_name  Test Organization
    Populate Fundraising Settings field  goal  100
    Select Fundraising Settings checkbox  allow_pf
    Click Button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Campaign")]/..
    Input text  form-widgets-IDublinCore-title  Test Campaign
    Click Button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  100
    Click Button  Cancel

    Go to  ${PLONE_URL}/test-settings
    Click Edit in edit bar
    Fundraising Settings value should be  goal  100
    Populate Fundraising Settings field  goal  200
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign
    Click Edit in edit bar
    Fundraising Campaign value should be  goal  200
    Populate Fundraising Campaign field  goal  300
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings
    Click Edit in edit bar
    Populate Fundraising Settings field  goal  400
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign
    Click Edit in edit bar
    Fundraising Campaign value should be  goal  300
    Click Button  Cancel
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
