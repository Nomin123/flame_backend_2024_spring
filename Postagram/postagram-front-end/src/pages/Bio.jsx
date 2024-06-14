import React from "react";
import Header from "./Header";
import Post from "./Post";

function Bio() {
  return (
    <div>
      <Header />
      <div className="flex gap-[50px] justify-center mt-[20px] items-center">
        <img
          className="flex content-center w-[95px] h-[95px] rounded-full "
          src="https://api.dicebear.com/7.x/pixel-art/svg"
          alt=""
        />
        <div>
          (No bio.)
          <h6>1 posts</h6>
        </div>
      </div>
      <hr />
      <div className="ml-[500px]">
        <Post />
      </div>
    </div>
  );
}

export default Bio;
