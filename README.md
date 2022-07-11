# ロールでユーザー管理を行っているサーバーの為のユーザー認証bot
## 使い方
1.discord developer portalよりtokenの発行  
2.サーバーへ1で作成したbotの導入  
3.サーバーで認証済のユーザーに付与するロールを作成  
4.config.pyにトークンと3で作成したロールの名前を入力  
5.実行  
  
認証コマンド : `/auth`  
※`/`の部分はconfig.pyのcommand_prefixで設定した値が用いられます。  
  
## config.pyについて
|変数名|内容|
|--|--|
|discord_token|取得したdiscord botのトークン|
|role_name|認証が完了した際に付与されるロールの名称|
|timeout|ユーザーが認証コードを入力しなかった場合のタイムアウト時間|
|command_prefix|コマンドのプレフィックス(デフォルトでは"/")|
