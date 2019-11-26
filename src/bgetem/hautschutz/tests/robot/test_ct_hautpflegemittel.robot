# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bgetem.hautschutz -t test_hautpflegemittel.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bgetem.hautschutz.testing.BGETEM_HAUTSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bgetem/hautschutz/tests/robot/test_hautpflegemittel.robot
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

Scenario: As a site administrator I can add a Hautpflegemittel
  Given a logged-in site administrator
    and an add Hautpflegemittel form
   When I type 'My Hautpflegemittel' into the title field
    and I submit the form
   Then a Hautpflegemittel with the title 'My Hautpflegemittel' has been created

Scenario: As a site administrator I can view a Hautpflegemittel
  Given a logged-in site administrator
    and a Hautpflegemittel 'My Hautpflegemittel'
   When I go to the Hautpflegemittel view
   Then I can see the Hautpflegemittel title 'My Hautpflegemittel'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Hautpflegemittel form
  Go To  ${PLONE_URL}/++add++Hautpflegemittel

a Hautpflegemittel 'My Hautpflegemittel'
  Create content  type=Hautpflegemittel  id=my-hautpflegemittel  title=My Hautpflegemittel

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Hautpflegemittel view
  Go To  ${PLONE_URL}/my-hautpflegemittel
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Hautpflegemittel with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Hautpflegemittel title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
