function OthersProfiles(props) {
    console.log(props)
  return (
    <div className="w-[350px] h-[800px] border-solid border-gray-100 border-2 rounded-lg">
      <h3 className=" text-blue-400 text-center">Others profiles</h3>
      <div className="flex gap-[10px] justify-center mt-[40px]">
        <img
          className="w-[50px] h-[50px] rounded-full bg-pink-100"
          src="https://api.dicebear.com/7.x/pixel-art/svg"
          alt=""
        />
        <button className="w-[120px] h-[45px] rounded-lg bg-blue-600 text-white">
          See profile
        </button>
      </div>
      
    </div>
  );
}

export default OthersProfiles;
