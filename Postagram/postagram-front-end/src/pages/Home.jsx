import React, { useState } from "react";
import Header from "./Header";
import CreatePost from "./CreatePost";
import { getUser } from "../hooks/user.actions";
import Post from "./Post";
import OthersProfiles from "./OthersProfiles";
import axiosService from "../helpers/axios";
import { useParams } from "react-router-dom";


function Home() {
  var user = getUser();
  const {profileId} = useParams();
  const [userPosts, setUserPosts] = useState([])
  const [show , setshow] = useState(true)
  // const posts = (`/post/?author_public_id=48dfd8dd2c1e4b3d865551bae9250dcd`, fetcher, {
  //   refreshInterval: 20000
  // })
  // console.log(posts?.data)
  axiosService
    .get(`/post/?author_public_id=${profileId}/`)
    .then((res) => {
      setUserPosts(res.data);
      // console.log(res);
    })
    .catch((error) => {
      console.error(error);
    });

  return (
    <div className="flex flex-col gap-[10px] border-solid border-gray-100 border-2 rounded-lg ">
      <Header />
      <div className="flex gap-[20px] justify-center">
        <div className="flex flex-col gap-[20px] border-solid border-gray-100 border-2 rounded-lg ">
          <CreatePost />
          {/* {userPosts && 
            userPosts.map((post, index) => (
              <Post key={index} post={post} refresh={post.mutate}/>
            ))} */}
          
        </div>
        <div>
          <OthersProfiles />
          {/* {user.data?.map((u, index) => <OthersProfiles key={index} user={u}/>)} */}
        </div>
      </div>
      my name is {user.username}
      <button className="w-[30px] bg-black h-[30px]" onClick={()=>
        setshow(!show)}>
          {show ? (
            <div>
              asdkfj
            </div>
          ) : (
            <div>
              qwer
            </div>
          )}
        hi
      </button>
    </div>
  );
}

export default Home;
