#!/bin/bash

set -e

PROJECT_DIR="${PROJECT_DIR:-$WORKSPACE}"
WORKSPACE="My Demo App.xcworkspace"
SCHEME="My Demo App"
DEVICE_NAME="iPhone 17 Pro"
DERIVED_DATA="build"
APP_PATH="$PROJECT_DIR/$DERIVED_DATA/Build/Products/Debug-iphonesimulator/My Demo App.app"

cd "$PROJECT_DIR"

if [ -f "Podfile" ]; then
  pod install
fi

if [ -d "$WORKSPACE" ]; then
  xcodebuild \
    -workspace "$WORKSPACE" \
    -scheme "$SCHEME" \
    -sdk iphonesimulator \
    -configuration Debug \
    -derivedDataPath "$DERIVED_DATA"
else
  xcodebuild \
    -project "My Demo App.xcodeproj" \
    -scheme "$SCHEME" \
    -sdk iphonesimulator \
    -configuration Debug \
    -derivedDataPath "$DERIVED_DATA"
fi

xcrun simctl boot "$DEVICE_NAME" || true
open -a Simulator

xcrun simctl install booted "$APP_PATH"

BUNDLE_ID=$(xcrun simctl listapps booted | grep -i "demo" | grep -o '"CFBundleIdentifier" = "[^"]*"' | sed 's/"CFBundleIdentifier" = "//;s/"//' | head -1)
if [ -n "$BUNDLE_ID" ]; then
  xcrun simctl launch booted "$BUNDLE_ID"
fi

echo "iOS build + install complete."
