import requests
from jsonpath_ng import jsonpath, parse
import json
import csv
import time

from save_reweeters import get_all_reweeters_and_save
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
    'personalization_id': '"v1_BC5O1BWnF756yk0KLdcoMg=="',
}

headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'des_opt_in=Y; _gcl_au=1.1.471506689.1684744541; guest_id=v1%3A168533894350591863; guest_id_marketing=v1%3A168533894350591863; guest_id_ads=v1%3A168533894350591863; g_state={"i_l":0}; kdt=3zLzd30xQqC6dXelc5prRStiSsPQSZdqoUT7Dcfu; auth_token=f681146a65d46e355b39c685e74e7d827e92780d; ct0=e915ffe760dcf033a5a860584931bfad0a8e2173759fbb736aa9364b7d8e65d4d15fd568ead5064168077b627b5c5c5da08443d9ecdbfee1d56f7d1fe4e0b05e7ac9514468650c257d8e18d926b44daf; twid=u%3D1663059805496545282; at_check=true; _gid=GA1.2.668880270.1692021343; lang=en; external_referer=padhuUp37zjgzgv1mFWxJ5Xq0CLV%2BbpWuS41v6lN3QU%3D|0|8e8t2xd8A2w%3D; mbox=PC#31e5c2956f6b4fe1887060d9d323c0b3.38_0#1755311886|session#9ee1af3804264054a21008ab893415d2#1692068946; _ga_34PHSZMC42=GS1.1.1692067100.32.0.1692067100.0.0.0; _ga=GA1.2.1234823805.1684386389; personalization_id="v1_BC5O1BWnF756yk0KLdcoMg=="',
    'pragma': 'no-cache',
    'referer': 'https://twitter.com/EliotHiggins/status/1637927681734987777/retweets/with_comments',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-client-transaction-id': 'nRcChf3aveIpNcoxVTlWsED4j3pYoyslJM5PDz1jqH/0+GVPKONTCIALnZq2BfPSTpwlFp1fE1FMTTT1dh518sf3Wjx6nA',
    'x-client-uuid': 'f9c04e63-268b-41c9-a8a6-ea37beaa4f41',
    'x-csrf-token': 'e915ffe760dcf033a5a860584931bfad0a8e2173759fbb736aa9364b7d8e65d4d15fd568ead5064168077b627b5c5c5da08443d9ecdbfee1d56f7d1fe4e0b05e7ac9514468650c257d8e18d926b44daf',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}

def get_quoters(tweetId,cursor = None):
    time.sleep(15)
    variables = {"rawQuery":f"quoted_tweet_id:{tweetId}","count":100,"querySource":"tdqt","product":"Top"}
    if cursor is not None:
        variables['cursor'] = cursor
    variables_str = json.dumps(variables)

    params = {
        'variables': variables_str,
        'features': '{"rweb_lists_timeline_redesign_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    }

    while True:
        try:
            response = requests.get('https://twitter.com/i/api/graphql/NA567V_8AFwu0cZEkAAKcw/SearchTimeline', params=params, cookies=cookies, headers=headers)
            print(response.text)
            json_data = response.json()
            break
        except:
            print(response.text)
            time.sleep(300)


    screen_name_path ='$.data.search_by_raw_query.search_timeline.timeline.instructions[*].entries[*].content.itemContent.tweet_results.result.core.user_results.result.legacy.screen_name'
    screen_name_expression = parse(screen_name_path)
    screen_names1 = [match.value for match in screen_name_expression.find(json_data)]

    screen_name_path ='$.data.search_by_raw_query.search_timeline.timeline.instructions[*].entries[*].content.itemContent.tweet_results.result.tweet.core.user_results.result.legacy.screen_name'
    screen_name_expression = parse(screen_name_path)
    screen_names2 = [match.value for match in screen_name_expression.find(json_data)]

    screen_names = screen_names1 + screen_names2

                      #data.search_by_raw_query.search_timeline.timeline.instructions[0].entries[1].content.itemContent.tweet_results.result.legacy.full_text
    quotext_path = '$.data.search_by_raw_query.search_timeline.timeline.instructions[*].entries[*].content.itemContent.tweet_results.result.legacy.full_text'
    quotext_name_expression = parse(quotext_path)
    quotexts1 = [match.value for match in quotext_name_expression.find(json_data)]


    quotext_path = '$.data.search_by_raw_query.search_timeline.timeline.instructions[*].entries[*].content.itemContent.tweet_results.result.tweet.legacy.full_text'
    quotext_name_expression = parse(quotext_path)
    quotexts2 = [match.value for match in quotext_name_expression.find(json_data)]

    quotexts =quotexts1 + quotexts2


    conversitionIdPath = '$.data.search_by_raw_query.search_timeline.timeline.instructions[*].entries[*].content.itemContent.tweet_results.result.legacy.conversation_id_str'
    conversitionId_expression = parse(conversitionIdPath)
    conversitionIds1 = [match.value for match in conversitionId_expression.find(json_data)]


    conversitionIdPath = '$.data.search_by_raw_query.search_timeline.timeline.instructions[*].entries[*].content.itemContent.tweet_results.result.tweet.legacy.conversation_id_str'
    conversitionId_expression = parse(conversitionIdPath)
    conversitionIds2 = [match.value for match in conversitionId_expression.find(json_data)]
    conversitionIds = conversitionIds1 + conversitionIds2

    path1 = 'data.search_by_raw_query.search_timeline.timeline.instructions[0].entries[-1].content.value'
    token_expression1 = parse(path1)
    next_token1 = [match.value for match in token_expression1.find(json_data)]

    token_path = 'data.search_by_raw_query.search_timeline.timeline.instructions[2].entry.content.value'
    token_expression = parse(token_path)
    next_token2 = [match.value for match in token_expression.find(json_data)]
    next_token = next_token1 + next_token2
    if len(next_token) >0:
        next_token = next_token[0]
    else:
        next_token = None

    # print(next_token)
    #
    # print(screen_names)
    # print(quotexts)
    # print(conversitionIds)

    return screen_names, quotexts,conversitionIds,next_token


def get_all_get_quoters(tweetId):
    next_token = None
    all_screen_names = []
    all_quotexts = []
    all_conversitionIds = []
    while True:
        screen_names, quotexts, conversitionIds, next_token = get_quoters(tweetId,next_token)
        print("nexttoen:",next_token)
        if len(screen_names) ==0:
            break
        all_screen_names += screen_names
        all_quotexts += quotexts
        all_conversitionIds += conversitionIds
    return all_screen_names,all_quotexts,all_conversitionIds

tweetId = '1637927681734987777'
author_sceen_name = 'EliotHiggins'

all_screen_names,all_quotexts,conversitionIds = get_all_get_quoters(tweetId)
with open("1637927681734987777.csv",'a') as f:
    fw = csv.writer(f)
    for i in range(len(all_screen_names)):
        screen_name = all_screen_names[i]
        text = all_quotexts[i]
        conversitionId = conversitionIds[i]
        fw.writerow([screen_name,author_sceen_name,text,conversitionId,tweetId])
        f.flush()

print('start 2:')
print(len(conversitionIds))

with open("1637927681734987777.csv",'a') as f:
    fw = csv.writer(f)
    for i in range(len(all_screen_names)):
        screen_name = all_screen_names[i]
        text = all_quotexts[i]
        conversitionId = conversitionIds[i]
        print(i)
        all_screen_names2, all_quotexts2, conversitionIds2 = get_all_get_quoters(conversitionId)
        for j in range(len(all_screen_names2)):
            screen_name2 = all_screen_names2[j]
            text2 = all_quotexts2[j]
            conversitionId2 = conversitionIds2[j]
            fw.writerow([screen_name2, screen_name, text2, conversitionId2, conversitionId])
            f.flush()



