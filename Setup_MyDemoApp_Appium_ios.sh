#!/bin/bash

# ─────────────────────────────────────────────────────────────
# 8/12 - iOS Simulator + Appium Inspector — One-Click Setup Script
#
# Project: My Demo App
#
# Jenkins usage:
#   ./Setup_MyDemoApp_Appium_ios.sh --jenkins
#
# Jenkins mode:
#   - Builds the application
#   - Boots the simulator if necessary
#   - Installs the application
#   - Determines the bundle ID
#   - Launches the application
#   - Does NOT start Appium
#
# Normal/manual usage:
#   ./Setup_MyDemoApp_Appium_ios.sh
#
# Normal mode:
#   - Performs all setup steps
#   - Starts Appium in the foreground
# ─────────────────────────────────────────────────────────────

set -e

# ─────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────

PROJECT_DIR="$HOME/Desktop/my-demo-app-ios-main"

WORKSPACE="My Demo App.xcworkspace"
PROJECT_FILE="My Demo App.xcodeproj"
SCHEME="My Demo App"

DEVICE_NAME="iPhone 17 Pro"

DERIVED_DATA="build"

APP_PATH="$PROJECT_DIR/$DERIVED_DATA/Build/Products/Debug-iphonesimulator/My Demo App.app"

# Jenkins mode
JENKINS_MODE=false

if [ "$1" = "--jenkins" ]; then
    JENKINS_MODE=true
fi

# ─────────────────────────────────────────────────────────────
# Colours
# ─────────────────────────────────────────────────────────────

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# ─────────────────────────────────────────────────────────────
# Logging functions
# ─────────────────────────────────────────────────────────────

log() {
    echo -e "${GREEN}✔ $1${NC}"
}

warn() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

fail() {
    echo -e "${RED}✖ $1${NC}"
    exit 1
}

# ─────────────────────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────────────────────

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  iOS Simulator + Appium Inspector — Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ "$JENKINS_MODE" = true ]; then
    echo "Running in Jenkins mode."
    echo "Jenkins will manage the Appium server."
    echo ""
fi

# ─────────────────────────────────────────────────────────────
# Step 1: Navigate to project
# ─────────────────────────────────────────────────────────────

echo "▶ Step 1: Checking project directory..."

if [ ! -d "$PROJECT_DIR" ]; then
    fail "Project folder not found at: $PROJECT_DIR"
fi

cd "$PROJECT_DIR"

log "Found project at $PROJECT_DIR"

# ─────────────────────────────────────────────────────────────
# Step 2: Install pods if Podfile exists
# ─────────────────────────────────────────────────────────────

echo ""
echo "▶ Step 2: Checking for Podfile..."

if [ -f "Podfile" ]; then

    warn "Podfile found — running pod install..."

    if ! command -v pod >/dev/null 2>&1; then
        fail "CocoaPods is not installed. Run: sudo gem install cocoapods"
    fi

    pod install

    log "Pods installed"

else

    log "No Podfile found — skipping pod install"

fi

# ─────────────────────────────────────────────────────────────
# Step 3: Build for simulator
# ─────────────────────────────────────────────────────────────

echo ""
echo "▶ Step 3: Building app for simulator..."

BUILD_LOG="$PROJECT_DIR/xcodebuild.log"

rm -f "$BUILD_LOG"

if [ -d "$WORKSPACE" ]; then

    echo "Using workspace: $WORKSPACE"

    if xcodebuild \
        -workspace "$WORKSPACE" \
        -scheme "$SCHEME" \
        -sdk iphonesimulator \
        -configuration Debug \
        -derivedDataPath "$DERIVED_DATA" \
        > "$BUILD_LOG" 2>&1; then

        log "Build succeeded"

    else

        echo ""
        echo "xcodebuild output:"
        echo "────────────────────────────────────────────"

        tail -n 100 "$BUILD_LOG"

        echo "────────────────────────────────────────────"

        fail "Build failed. Full build log: $BUILD_LOG"

    fi

elif [ -d "$PROJECT_FILE" ]; then

    warn ".xcworkspace not found — falling back to .xcodeproj"

    if xcodebuild \
        -project "$PROJECT_FILE" \
        -scheme "$SCHEME" \
        -sdk iphonesimulator \
        -configuration Debug \
        -derivedDataPath "$DERIVED_DATA" \
        > "$BUILD_LOG" 2>&1; then

        log "Build succeeded"

    else

        echo ""
        echo "xcodebuild output:"
        echo "────────────────────────────────────────────"

        tail -n 100 "$BUILD_LOG"

        echo "────────────────────────────────────────────"

        fail "Build failed. Full build log: $BUILD_LOG"

    fi

else

    fail "No .xcworkspace or .xcodeproj found in $PROJECT_DIR"

fi

# ─────────────────────────────────────────────────────────────
# Step 4: Boot simulator
# ─────────────────────────────────────────────────────────────

echo ""
echo "▶ Step 4: Booting simulator..."

echo "Requested simulator:"
echo "$DEVICE_NAME"

echo ""

# Find the UDID for the requested simulator.

UDID=$(
    xcrun simctl list devices available |
    grep -F "$DEVICE_NAME" |
    grep -oE '[A-F0-9-]{36}' |
    head -n 1
)

if [ -z "$UDID" ]; then
    fail "Could not find simulator: $DEVICE_NAME"
fi

echo "Simulator:"
echo "$DEVICE_NAME"

echo "UDID:"
echo "$UDID"

echo ""

# Check whether this exact simulator is already booted.

DEVICE_STATE=$(
    xcrun simctl list devices |
    grep "$UDID" |
    grep -oE '\((Booted|Shutdown)\)' |
    head -n 1 |
    tr -d '()'
)

if [ "$DEVICE_STATE" = "Booted" ]; then

    log "Simulator already booted: $DEVICE_NAME ($UDID)"

else

    echo "Booting simulator..."

    xcrun simctl boot "$UDID" 2>/dev/null || true

    echo "Waiting for simulator to finish booting..."

    xcrun simctl bootstatus "$UDID" -b

    log "Simulator is ready"

fi

# ─────────────────────────────────────────────────────────────
# Step 5: Install app
# ─────────────────────────────────────────────────────────────

echo ""
echo "▶ Step 5: Installing app on simulator..."

if [ ! -d "$APP_PATH" ]; then

    fail "App not found at:

$APP_PATH

Run:

find $PROJECT_DIR/$DERIVED_DATA -name '*.app'

to locate the application."

fi

echo "Installing:"
echo "$APP_PATH"

xcrun simctl install "$UDID" "$APP_PATH" \
    || fail "Failed to install app on simulator."

log "App installed: $APP_PATH"

# ─────────────────────────────────────────────────────────────
# Step 6: Determine bundle ID and launch app
# ─────────────────────────────────────────────────────────────

echo ""
echo "▶ Step 6: Launching app..."

INFO_PLIST="$APP_PATH/Info.plist"

if [ ! -f "$INFO_PLIST" ]; then
    fail "Info.plist not found at: $INFO_PLIST"
fi

# Read the bundle identifier directly from the built application.

BUNDLE_ID=$(
    /usr/libexec/PlistBuddy \
    -c "Print :CFBundleIdentifier" \
    "$INFO_PLIST" 2>/dev/null
)

if [ -z "$BUNDLE_ID" ]; then
    fail "Could not determine bundle ID from $INFO_PLIST"
fi

echo "Bundle ID:"
echo "$BUNDLE_ID"

echo ""

# Verify that the application is actually installed.

if ! xcrun simctl listapps "$UDID" | grep -q "\"$BUNDLE_ID\""; then
    fail "Application $BUNDLE_ID is not installed on simulator $UDID"
fi

echo "Launching application..."

xcrun simctl launch "$UDID" "$BUNDLE_ID" \
    || fail "Could not launch application with bundle ID: $BUNDLE_ID"

log "App launched with bundle ID: $BUNDLE_ID"

# ─────────────────────────────────────────────────────────────
# Step 7: Check Appium
# ─────────────────────────────────────────────────────────────

echo ""
echo "▶ Step 7: Checking Appium..."

if ! command -v appium >/dev/null 2>&1; then

    warn "Appium not found — installing..."

    if ! command -v npm >/dev/null 2>&1; then
        fail "npm is not installed. Cannot install Appium."
    fi

    npm install -g appium

    appium driver install xcuitest

    log "Appium installed"

else

    APPIUM_VERSION=$(appium --version)

    log "Appium already installed: $APPIUM_VERSION"

fi

# ─────────────────────────────────────────────────────────────
# Jenkins mode
#
# IMPORTANT:
#
# Do NOT start Appium here when running from Jenkins.
#
# Jenkins will start Appium in its own stage so that:
#
#   Setup script
#          ↓
#   returns control to Jenkins
#          ↓
#   Jenkins starts Appium
#          ↓
#   Jenkins runs pytest
#
# ─────────────────────────────────────────────────────────────

if [ "$JENKINS_MODE" = true ]; then

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  Jenkins Setup Complete"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Simulator:     $DEVICE_NAME"
    echo "UDID:          $UDID"
    echo "Bundle ID:     $BUNDLE_ID"
    echo "App:           $APP_PATH"
    echo "Appium:        $APPIUM_VERSION"
    echo ""
    echo "App has been built, installed, and launched."
    echo ""
    echo "Jenkins will now start and manage the Appium server."
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    exit 0

fi

# ─────────────────────────────────────────────────────────────
# Normal/manual mode
#
# When this script is run manually, Appium is started in the
# foreground as it was in the original script.
# ─────────────────────────────────────────────────────────────

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Setup complete! Appium is starting..."
echo ""
echo "  Appium Inspector capabilities:"
echo ""
echo "  {"
echo '    "platformName": "iOS",'
echo '    "appium:automationName": "XCUITest",'
echo "    \"appium:deviceName\": \"$DEVICE_NAME\","
echo '    "appium:platformVersion": "26.5",'
echo "    \"appium:app\": \"$APP_PATH\","
echo "    \"appium:udid\": \"$UDID\""
echo "  }"
echo ""
echo "  Remote host: 127.0.0.1  |  Port: 4723  |  Path: /"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

appium