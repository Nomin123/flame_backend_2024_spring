function Post(props) {
  console.log(props)
  return (
    <div className="w-[700px] h-[300px] border-solid rounded-lg border-1 border-gray flex flex-col gap-[10px] p-[20px]">
      <div className="flex gap-[500px]">
      <div className="flex gap-[12px] justify-left items-center p-[20px]">
        <img
          className="w-[50px] h-[50px] rounded-full"
          src="https://api.dicebear.com/7.x/pixel-art/svg"
          alt=""
        />
        <h6>1 day ago</h6>
      </div>
      <div>
        <button><img className="w-[20px] h-[20px]" src="dots-vertical-rounded-regular-24.png"  alt="" /></button>
      </div>
      </div>
      <p className="pl-[25px]">{props.post?.body}</p>
      <div className="flex gap-[10px] pl-[15px]">
        <img
          className="w-[25px] h-[25px] rounded-full bg-red-100 items-center justify-center"
          src="like.png"
          alt=""
        />
        0 likes
      </div>
      <div className="pl-[20px]"> <a href="/comment"> comment</a></div>
      <div className="flex gap-[15px] pt-[20px]">
        <div className="flex gap-[5px] content-center pl-[20px]">
          <img className="w-[20px] h-[20px]" src="like-regular-24.png" alt="" />
          like
        </div>
        <div className="flex gap-[5px] content-center">
          <img
            className="w-[20px] h-[20px]"
            src="message-rounded-dots-regular-24.png"
            alt=""
          />
          Comment
        </div>
      </div>
    </div>
  );
}

export default Post;
