# velvet

はてなブログの記事のコンテンツから、ブックマーク数を予測するwebアプリです。

開発背景や方法など、詳細は[こちらの記事](https://pompom168.hatenablog.com/entry/2020/01/21/080000)を参照ください。

![about](https://user-images.githubusercontent.com/12094957/72904052-9e9e6180-3d71-11ea-8dff-e32261aa024d.png)

## アーキテクチャ

このwebアプリ自体は。gunicorn上のFlaskで実装されており、EC2インスタンス上で起動しています。

任意のURLから記事をスクレイピングして、ブックマーク数を予測するAPI ([velvet-api](https://github.com/kishimoto-banana/velvet-api)) が別で動いています。それはfastapiで実装され、別のEC2インスタンス上で起動しています。

![arc_pre](https://user-images.githubusercontent.com/12094957/72904345-17052280-3d72-11ea-8841-dda6025c3a29.png)

## ローカルでの実行方法

docker-composeを使用して、アプリケーションを実行します。

```bash
$ docker-compose up -d
```

[velvet-api](https://github.com/kishimoto-banana/velvet-api)の実行も必要です。
