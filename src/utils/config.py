base_url = "https://m.twitch.tv"
timeout = 10

# Emulation settings for different devices
# These settings are used to emulate different devices in the tests.
# The settings include device metrics such as width, height, and pixel ratio,
# as well as the user agent string that will be used in the requests.
# The user agent string is important for simulating the behavior of different devices
# and browsers.
iphone_12_emulation = {
    "deviceMetrics": {
        "width": 390,
        "height": 844,
        "pixelRatio": 3.0
    },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
}

iphone_15_emulation = {
    "deviceMetrics": {
        "width": 393,
        "height": 852,
        "pixelRatio": 3.0
    },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
}

samsung_galaxy_s20_ultra_emulation = {
    "deviceMetrics": {
        "width": 412,
        "height": 915,
        "pixelRatio": 3.5
    },
    "userAgent": "Mozilla/5.0 (Linux; Android 10; SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"
}

pixel_7_emulation = {
    "deviceMetrics": {
        "width": 412,
        "height": 869,
        "pixelRatio": 3.5
    },
    "userAgent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
}
