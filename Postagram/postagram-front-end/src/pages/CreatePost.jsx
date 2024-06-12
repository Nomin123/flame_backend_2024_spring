import { useState } from "react";
import { getUser } from "../hooks/user.actions";
import axiosService from "../helpers/axios";

function CreatePost() {
  const user = getUser();
  const [post, setPost] = useState("");
  const [validated, setvalidated] = useState(false);
  console.log(user);
  const handleSubmit = (event) => {


    setvalidated(true);

    const data = {
      author: user.id,
      body: post,
    };

    console.log(data)

    axiosService
      .post("/post/", data)
      .then((res) => {
        console.log(res);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className=" w-[700px] h-[120px] p-[30px] rounded-lg border flex gap-[20px] items-center justify-left">
      <img
        className="w-[95px] h-[95px] border-grey-200 rounded-full border-solid"
        src="https://api.dicebear.com/7.x/pixel-art/svg"
        alt=""
      />
      <input
        type="text"
        className="w-[500px] h-[50px] rounded-full border-gray-100 bg-sky-100  border-solid pl-[20px] "
        placeholder="Write post"
        onChange={(event) => setPost(event.target.value)}
      />
      <button className="bg-blue-300 rounded-lg" onClick={handleSubmit}>
        post me
      </button>

      {/* <div className="hidden w-[500px] h-[500px] border-solid rounded-lg border-blue-100 bg-amber-100">
          <h1 className="h-[80px] bg-pink-100">Create Post</h1>
          <textarea name="" id="" cols="30" rows="10" className="w-[400px] h-[400px] border-solid border-gray-300 border-2 rounded-lg"></textarea>
        </div> */}
    </div>
  );
}

export default CreatePost;
