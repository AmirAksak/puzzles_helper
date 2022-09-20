[app]

title = Puzzles Helper
package.name = mobileapp001
package.domain = org.wiseplat
source.dir = .


#source.include_exts = py,png,jpg,kv,atlas,po,mo
#source.include_patterns = assets/*,images/*.png
#source.exclude_exts = spec
#source.exclude_dirs = tests, bin, venv
#source.exclude_patterns = license,images/*/*.jpg


version = 0.1

requirements = python3,kivy==2.1.0,pyperclip


presplash.filename = %(source.dir)/images/kiril.png

orientation = portrait


osx.python_version = 3
osx.kivy_version = 2.1.0


fullscreen = 1


android.arch = armeabi-v7a

android.allow_backup = True


ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master


ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0


ios.codesign.allowed = false


[buildozer]


log_level = 2


warn_on_root = 1

