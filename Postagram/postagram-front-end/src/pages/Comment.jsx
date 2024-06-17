import Header from "./Header";
import Post from "./Post";
import CreatePost from "./CreatePost";

function Comment() {
  return (
    <div className="flex flex-col gap-[10px] justify-center items-center">
      <Header />
      <Post />
      <div className="flex gap-[20px] justify-center items-center">
        <CreatePost />
        {/* <button className="w-[150px] h-[50px] bg-slate-400 rounded-lg">Comment</button> */}
      </div>
    </div>
  );
}

export default Comment;
