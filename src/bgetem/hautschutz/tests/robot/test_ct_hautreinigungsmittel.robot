# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bgetem.hautschutz -t test_hautreinigungsmittel.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bgetem.hautschutz.testing.BGETEM_HAUTSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bgetem/hautschutz/tests/robot/test_hautreinigungsmittel.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Hautreinigungsmittel
  Given a logged-in site administrator
    and an add Hautreinigungsmittel form
   When I type 'My Hautreinigungsmittel' into the title field
    and I submit the form
   Then a Hautreinigungsmittel with the title 'My Hautreinigungsmittel' has been created

Scenario: As a site administrator I can view a Hautreinigungsmittel
  Given a logged-in site administrator
    and a Hautreinigungsmittel 'My Hautreinigungsmittel'
   When I go to the Hautreinigungsmittel view
   Then I can see the Hautreinigungsmittel title 'My Hautreinigungsmittel'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Hautreinigungsmittel form
  Go To  ${PLONE_URL}/++add++Hautreinigungsmittel

a Hautreinigungsmittel 'My Hautreinigungsmittel'
  Create content  type=Hautreinigungsmittel  id=my-hautreinigungsmittel  title=My Hautreinigungsmittel

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Hautreinigungsmittel view
  Go To  ${PLONE_URL}/my-hautreinigungsmittel
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Hautreinigungsmittel with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Hautreinigungsmittel title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
