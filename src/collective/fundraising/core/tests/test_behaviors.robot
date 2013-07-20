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

Fields for behavior Fundraising Settings are available
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Fundraising Settings
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
    Select Fundraising Settings checkbox  allow_personal
    Populate Fundraising Settings field  completion_threshold  25
    Populate Fundraising Settings field  completion_threshold  10
    Click Button  Save

    Wait until page contains  link=Edit
    Populate Fundraising Settings field  completion_threshold  15
    Populate Fundraising Settings field  completion_threshold  5
    Click Button  Save

    

*** Keywords ***

Start browser
    Open browser  ${PLONE_URL}

Create dexterity type
    [Arguments]  ${title}
    Go to  ${PLONE_URL}/@@dexterity-types
    Click Overlay Button  css=#add-type input
    Input Text  css=#formfield-form-widgets-title input  ${title}
    Click Button  Add
    Wait until page contains element  link=Behaviors

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
    Input text  form-widgets-IFundraisingSettings-cf_fs_${name}  ${value}

Select Fundraising Settings checkbox
    [Arguments]  ${name}
    Select checkbox  form-widgets-IFundraisingSettings-cf_fs_${name}-0
