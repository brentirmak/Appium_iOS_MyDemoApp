#!/bin/bash

# ─────────────────────────────────────────────────────────────
#  iOS Simulator + Appium Inspector — One-Click Setup Script
#  Project: My Demo App
# ─────────────────────────────────────────────────────────────

set -e  # Exit immediately on any error

PROJECT_DIR="$HOME/Desktop/my-demo-app-ios-main"
WORKSPACE="My Demo App.xcworkspace"
SCHEME="My Demo App"
DEVICE_NAME="iPhone 17 Pro"
DERIVED_DATA="build"
APP_PATH="$PROJECT_DIR/$DERIVED_DATA/Build/Products/Debug-iphonesimulator/My Demo App.app"

# ── Colours for output ──────────────────────────────────────
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Colour

log()  { echo -e "${GREEN}✔ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠ $1${NC}"; }
fail() { echo -e "${RED}✖ $1${NC}"; exit 1; }

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  iOS Simulator + Appium Inspector — Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# ── Step 1: Navigate to project ─────────────────────────────
echo "▶ Step 1: Checking project directory..."
cd "$PROJECT_DIR" || fail "Project folder not found at $PROJECT_DIR"
log "Found project at $PROJECT_DIR"

# ── Step 2: Install pods if Podfile exists ───────────────────
echo ""
echo "▶ Step 2: Checking for Podfile..."
if [ -f "Podfile" ]; then
  warn "Podfile found — running pod install..."
  pod install || fail "pod install failed. Is CocoaPods installed? Run: sudo gem install cocoapods"
  log "Pods installed"
else
  log "No Podfile found — skipping pod install"
fi

# ── Step 3: Build for simulator ─────────────────────────────
echo ""
echo "▶ Step 3: Building app for simulator..."
if [ -d "$WORKSPACE" ]; then
  xcodebuild \
    -workspace "$WORKSPACE" \
    -scheme "$SCHEME" \
    -sdk iphonesimulator \
    -configuration Debug \
    -derivedDataPath "$DERIVED_DATA" \
    | grep -E "^(Build|error:|warning:|.*succeeded|.*failed)" \
    || fail "Build failed"
elif [ -d "My Demo App.xcodeproj" ]; then
  warn ".xcworkspace not found — falling back to .xcodeproj"
  xcodebuild \
    -project "My Demo App.xcodeproj" \
    -scheme "$SCHEME" \
    -sdk iphonesimulator \
    -configuration Debug \
    -derivedDataPath "$DERIVED_DATA" \
    | grep -E "^(Build|error:|warning:|.*succeeded|.*failed)" \
    || fail "Build failed"
else
  fail "No .xcworkspace or .xcodeproj found in $PROJECT_DIR"
fi
log "Build succeeded"

# ── Step 4: Boot simulator ───────────────────────────────────
echo ""
echo "▶ Step 4: Booting simulator..."
BOOTED=$(xcrun simctl list devices | grep "Booted" | head -1)
if [ -n "$BOOTED" ]; then
  log "Simulator already booted: $BOOTED"
else
  warn "No booted simulator found — booting $DEVICE_NAME..."
  xcrun simctl boot "$DEVICE_NAME" || fail "Could not boot $DEVICE_NAME. Check available devices with: xcrun simctl list devices available"
  log "Booted $DEVICE_NAME"
fi
open -a Simulator

# ── Step 5: Install app on simulator ────────────────────────
echo ""
echo "▶ Step 5: Installing app on simulator..."
if [ ! -d "$APP_PATH" ]; then
  fail "App not found at: $APP_PATH\nRun: find $PROJECT_DIR/build -name '*.app' to locate it"
fi
xcrun simctl install booted "$APP_PATH" || fail "Failed to install app. Is the simulator booted?"
log "App installed: $APP_PATH"

# ── Step 6: Launch app ───────────────────────────────────────
echo ""
echo "▶ Step 6: Launching app..."
BUNDLE_ID=$(xcrun simctl listapps booted | grep -i "demo" | grep -o '"CFBundleIdentifier" = "[^"]*"' | sed 's/"CFBundleIdentifier" = "//;s/"//' | head -1)
if [ -z "$BUNDLE_ID" ]; then
  warn "Could not auto-detect bundle ID. Launch the app manually in the Simulator."
else
  xcrun simctl launch booted "$BUNDLE_ID"
  log "App launched with bundle ID: $BUNDLE_ID"
fi

# ── Step 7: Start Appium ─────────────────────────────────────
echo ""
echo "▶ Step 7: Checking Appium..."
if ! command -v appium &> /dev/null; then
  warn "Appium not found — installing..."
  npm install -g appium || fail "npm install failed. Is Node.js installed?"
  appium driver install xcuitest || fail "XCUITest driver install failed"
  log "Appium installed"
else
  log "Appium already installed: $(appium --version)"
fi

echo ""
echo "▶ Starting Appium server..."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Setup complete! Appium is starting..."
echo ""
echo "  Next: Open Appium Inspector and use these capabilities:"
echo ""
echo '  {'
echo '    "platformName": "iOS",'
echo '    "appium:automationName": "XCUITest",'
echo "    \"appium:deviceName\": \"$DEVICE_NAME\","
echo '    "appium:platformVersion": "26.5",'
echo "    \"appium:app\": \"$APP_PATH\","
echo '    "appium:udid": "booted"'
echo '  }'
echo ""
echo "  Remote host: 127.0.0.1  |  Port: 4723  |  Path: /"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

appium
