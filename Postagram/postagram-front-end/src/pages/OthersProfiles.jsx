function OthersProfiles(props) {
  console.log(props);
  return (
    <div className="w-[350px] h-[800px] border-solid border-gray-100 border-2 rounded-lg">
      <h3 className=" text-blue-400 text-center pt-[20px]">Others profiles</h3>
      <div className="flex gap-[15px] justify-center items-center mt-[40px]">
        <img
          className="w-[50px] h-[50px] rounded-full border-solid border-blue-500 border-2"
          src="https://api.dicebear.com/7.x/pixel-art/svg"
          alt=""
        />
        <a href="/profile">
        <button className="w-[120px] h-[45px] rounded-lg bg-blue-600 text-white hover:bg-sky-700">
          See profile
        </button>
        </a>
      </div>
      
    </div>
  );
}

export default OthersProfiles;
