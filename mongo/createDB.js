import { MongoClient } from "mongodb";

// .envがリンクがされないので、直打ち

// 接続情報の設定(admin)
const uri = `mongodb://root:pass@mongo:27017`;  // MongoDBサーバーのURI
const client = new MongoClient(uri);

// データベースおよびユーザー情報
const dbName = "blog";
const userName = "blog_user";
const password = "blog_pass";

async function main() {
  try {
    // MongoDBサーバーに接続
    await client.connect();
    console.log("Connected to MongoDB");

    // データベースとユーザーの作成
    const adminDb = client.db("admin"); // 管理用データベースに接続
    await adminDb.command({
      createUser: userName,
      pwd: password,
      roles: [{ role: "readWrite", db: dbName }]
    });
    console.log(`User '${userName}' created for database '${dbName}'`);

  } catch (error) {
    console.error("An error occurred:", error);
  } finally {
    // 接続を閉じる
    await client.close();
    console.log("Connection to MongoDB closed");
  }
}

// メイン関数を実行
main().catch(console.error);
