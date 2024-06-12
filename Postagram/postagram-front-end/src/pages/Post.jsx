function Post() {
  return (
    <div className="w-[700px] h-[300px] border-solid rounded-lg border-blue-500 bg-amber-200 flex flex-col gap-[10px] ">
      {/* my name is {user.username} */}
      <div className="flex gap-[12px] justify-left p-[20px]">
        <img
          className="w-[50px] h-[50px] rounded-full"
          src="https://api.dicebear.com/7.x/pixel-art/svg"
          alt=""
        />
        <p></p>
      </div>
      <p></p>
      <div className="flex gap-[10px]">
        <img className="w-[25px] h-[25px] rounded-full bg-red-100" src="like.png" alt="" />0 likes
      </div>
      <div>comment</div>
      <div>
        <div>
          <img src="" alt="" />
          like
        </div>
        <div>
          <img src="" alt="" />
          comment
        </div>
      </div>
    </div>
  );
}

export default Post;
