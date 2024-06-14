import React from "react";
import { getUser } from "../hooks/user.actions";
var user = getUser();

function Header(){
    return (
        <div className="flex flex-col gap-[20px] ">
          <div className="flex hover:space-x-8 w-[1200px] h-[100px] rounded-lg bg-blue-400 m-auto  space-x-4 items-center justify-between p-[15px]">
            <h2 className="text-white font-size-[24px] space-x-4">Postagram</h2>
            <div className="flex space-between gap-[12px] items-center p-[16px]  ">
              <h5 className="text-white content-between">Welcome! {user.email} </h5>
              <button className="w-[150px] h-[45px] rounded-lg bg-blue-500 text-white hover:bg-blue-700">
                Logout
              </button>
            </div>
          </div>
        </div>
      );
}

export default Header;