import React from "react";
import Header from "./Header";
import CreatePost from "./CreatePost";
import { getUser } from "../hooks/user.actions";

function Home() {
  var user = getUser();
  console.log(user)
  return(
    <div className="flex flex-col gap-[20px]">
     <Header />
     <CreatePost />
      my name is {user.username}
    </div>
  );
}

export default Home;
