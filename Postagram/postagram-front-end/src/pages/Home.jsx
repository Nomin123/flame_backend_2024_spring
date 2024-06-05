import React from "react";
function Home() {
  return (
    <div className="w-[800px] h-[430px] bg-slate-100 m-auto p-[30px] flex-col gap-[30px] " >
      <h1 className="text-[40px] font-black uppercase">Contact</h1>
      <div className="flex  gap-[20px]">
        <div>
          <label htmlFor="">Name</label> <br />
          <input type="text" placeholder="Name" className="pl-[20px] w-[360px] h-[40px] rounded-lg bg-slate-200"/>
        </div>
        <div>
          <label htmlFor="">Email</label> <br />
          <input type="text" placeholder="Email"  className="pl-[20px] w-[360px] h-[40px] rounded-lg bg-slate-200"/>
        </div>
      </div>
      <div>
        <label htmlFor=""  >Message</label> <br />
        <textarea name="" id="" cols="60" rows="5" placeholder="Messsage" className="w-[740px] h-[170px] rounded-lg p-[10px] bg-slate-200 mt-[8px]">
          
        </textarea>
      </div>
      <button className="w-[150px] h-[45px] bg-blue-950 rounded-lg text-white mt-[10px]" >Submit</button>
    </div>
  );
}
export default Home;
