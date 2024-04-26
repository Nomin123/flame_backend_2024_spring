import TimerForm from "./TimerForm";
import { useState } from "react";

export default function ToggleableTimerForm({ onFormSubmit }) {
    const [isOpen, setIsOpen] = useState(false);

    const handleFormOpen = () => {
        setIsOpen(true);
    };

    const handleFormClose = () => {
        setIsOpen(false);
    }

    const handleFormSubmit = (timer) => {
        onFormSubmit(timer);
        setIsOpen(false)
    };

    if (isOpen) {
        return (
            <TimerForm
                onFormSubmit={handleFormSubmit}
                onFormClose={handleFormClose}
            />
        );
    } else {
        return (
            <div className="bg-gray-100 p-4 flex justify-center w-1/3 m-auto">
                <button
                    className="bg-transparent hover:bg-blue-500 text-blue-700
                    font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded-full"
                    onClick={handleFormOpen}
                >
                    <i className="fas fa-plus">Open</i>
                </button>
            </div>
        );
    }
}