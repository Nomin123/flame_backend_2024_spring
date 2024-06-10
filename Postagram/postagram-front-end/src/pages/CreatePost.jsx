function CreatePost() {
    return(
        <div className=" m-auto w-[800px] h-[95px] rounded-lg border flex gap-[20px] items-center justify-left">
        <img
          className="w-[95px] h-[95px] border-grey-200 rounded-full border-solid bg-red-100"
          src=""
          alt=""
        />
        <input
          type="text"
          className="w-[500px] h-[60px] rounded-2xl border-grey-100 bg-sky-100 pl-[20px] border-solid"
          placeholder="Write post"
        />
      </div>
    );
}

export default CreatePost;