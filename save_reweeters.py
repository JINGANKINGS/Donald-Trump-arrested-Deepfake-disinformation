

import json
import requests
import time
import csv

cookies = {
    'des_opt_in': 'Y',
    '_gcl_au': '1.1.471506689.1684744541',
    'guest_id': 'v1%3A168533894350591863',
    'guest_id_marketing': 'v1%3A168533894350591863',
    'guest_id_ads': 'v1%3A168533894350591863',
    'g_state': '{"i_l":0}',
    'kdt': '3zLzd30xQqC6dXelc5prRStiSsPQSZdqoUT7Dcfu',
    'auth_token': 'f681146a65d46e355b39c685e74e7d827e92780d',
    'ct0': 'e915ffe760dcf033a5a860584931bfad0a8e2173759fbb736aa9364b7d8e65d4d15fd568ead5064168077b627b5c5c5da08443d9ecdbfee1d56f7d1fe4e0b05e7ac9514468650c257d8e18d926b44daf',
    'twid': 'u%3D1663059805496545282',
    'at_check': 'true',
    '_gid': 'GA1.2.668880270.1692021343',
    'lang': 'en',
    'external_referer': 'padhuUp37zjgzgv1mFWxJ5Xq0CLV%2BbpWuS41v6lN3QU%3D|0|8e8t2xd8A2w%3D',
    'mbox': 'PC#31e5c2956f6b4fe1887060d9d323c0b3.38_0#1755311886|session#9ee1af3804264054a21008ab893415d2#1692068946',
    '_ga_34PHSZMC42': 'GS1.1.1692067100.32.0.1692067100.0.0.0',
    '_ga': 'GA1.2.1234823805.1684386389',
    'personalization_id': '"v1_FGZa/h2eSQdUpkbcJclTqg=="',
}

headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'des_opt_in=Y; _gcl_au=1.1.471506689.1684744541; guest_id=v1%3A168533894350591863; guest_id_marketing=v1%3A168533894350591863; guest_id_ads=v1%3A168533894350591863; g_state={"i_l":0}; kdt=3zLzd30xQqC6dXelc5prRStiSsPQSZdqoUT7Dcfu; auth_token=f681146a65d46e355b39c685e74e7d827e92780d; ct0=e915ffe760dcf033a5a860584931bfad0a8e2173759fbb736aa9364b7d8e65d4d15fd568ead5064168077b627b5c5c5da08443d9ecdbfee1d56f7d1fe4e0b05e7ac9514468650c257d8e18d926b44daf; twid=u%3D1663059805496545282; at_check=true; _gid=GA1.2.668880270.1692021343; lang=en; external_referer=padhuUp37zjgzgv1mFWxJ5Xq0CLV%2BbpWuS41v6lN3QU%3D|0|8e8t2xd8A2w%3D; mbox=PC#31e5c2956f6b4fe1887060d9d323c0b3.38_0#1755311886|session#9ee1af3804264054a21008ab893415d2#1692068946; _ga_34PHSZMC42=GS1.1.1692067100.32.0.1692067100.0.0.0; _ga=GA1.2.1234823805.1684386389; personalization_id="v1_FGZa/h2eSQdUpkbcJclTqg=="',
    'pragma': 'no-cache',
    'referer': 'https://twitter.com/EliotHiggins/status/1637927681734987777/retweets',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-client-transaction-id': '0FILGfWSF2G0IKsx7fT0BTfIbyZohX5DD53Y5LfKfJQ4KX4Oqs8DQIf1rTm96YjoR8RMW9AuRTz82x4XJIKZQEaGtpeM0Q',
    'x-client-uuid': 'f9c04e63-268b-41c9-a8a6-ea37beaa4f41',
    'x-csrf-token': 'e915ffe760dcf033a5a860584931bfad0a8e2173759fbb736aa9364b7d8e65d4d15fd568ead5064168077b627b5c5c5da08443d9ecdbfee1d56f7d1fe4e0b05e7ac9514468650c257d8e18d926b44daf',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}


def get_reweeters(tweetId,cursor= None):
    variables = {
        'tweetId':tweetId,
        'count':100,
        'includePromotedContent':True
    }
    if cursor is not None:
        variables['cursor'] = cursor
    variables_str = json.dumps(variables)
    params = {
        'variables': variables_str,
        'features': '{"rweb_lists_timeline_redesign_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    }
    response = requests.get('https://twitter.com/i/api/graphql/_nBuZh82i3A0Ohkjw4FqCg/Retweeters', params=params, cookies=cookies, headers=headers)
    data = response.json()
    data = data['data']
    retweeters_timeline = data['retweeters_timeline']
    timeline = retweeters_timeline['timeline']
    instructions = timeline['instructions']
    screen_names = []
    next_cursor = None
    for instruction in instructions:
        if 'entries' not in instruction:
            return screen_names,None
        entries = instruction['entries']
        for entrie in entries:
            content = entrie['content']
            if 'cursorType' in content:
                if content['cursorType'] == 'Bottom':
                    next_cursor = content['value']
            else:
                user_results = content['itemContent']['user_results']
                try:
                    screen_name = user_results['result']['legacy']['screen_name']
                    screen_names.append(screen_name)
                except:
                    print(user_results)
    return screen_names,next_cursor

def get_all_reweeters(tweetId):
    next_cursor = None
    all_screen_names = []
    i = 0
    while True:
        screen_names, next_cursor = get_reweeters(tweetId,next_cursor)
        time.sleep(5)
        print(i)
        i+=1

        if len(screen_names) == 0:
            return all_screen_names
        all_screen_names += screen_names

    return all_screen_names


def get_all_reweeters_and_save(author_sceen_name,tweetId):
    all_screen_names = get_all_reweeters(tweetId)
    with open("1637927681734987777.csv",'a') as f:
        fw = csv.writer(f)
        for name in all_screen_names:
            fw.writerow([name,author_sceen_name])
            f.flush()

#tweet_sceen_name = 'EliotHiggins

#get_all_reweeters_and_save('EliotHiggins','1637927681734987777')