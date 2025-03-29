#!/bin/bash

# Exit on error
set -e

echo "Running Python tests..."
python3 scripts/test_integration.py

echo "Building Android project..."
cd android
./gradlew assembleDebug
cd ..

echo "Building iOS project..."
cd ios
pod install
xcodebuild -workspace StegAssimilator.xcworkspace -scheme StegAssimilator -configuration Debug -sdk iphonesimulator build
cd ..

echo "All tests passed and builds successful!" 