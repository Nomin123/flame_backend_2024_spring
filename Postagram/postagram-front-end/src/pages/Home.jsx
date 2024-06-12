import React from "react";
import Header from "./Header";
import CreatePost from "./CreatePost";
import { getUser } from "../hooks/user.actions";
import Post from "./Post";
import OthersProfiles from "./OthersProfiles";
import { fetcher } from "../helpers/axios";


function Home() {
  var user = getUser();
  const posts = (`/post/?author_public_id=48dfd8dd2c1e4b3d865551bae9250dcd`, fetcher, {
    refreshInterval: 20000
  })
  console.log(posts?.data)
  return (
    <div className="flex flex-col gap-[10px] border-solid border-gray-100 border-2 rounded-lg ">
      <Header />
      <div className="flex gap-[20px] justify-center">
        <div className="flex flex-col gap-[20px] border-solid border-gray-100 border-2 rounded-lg ">
          <CreatePost />
          <Post />
          
        </div>
        <div>
          <OthersProfiles />
          {/* {user.data?.map((u, index) => <OthersProfiles key={index} user={u}/>)} */}
        </div>
      </div>
      my name is {user.username}
    </div>
  );
}

export default Home;
