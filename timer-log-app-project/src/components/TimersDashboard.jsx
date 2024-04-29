import EditableTimerList from "./EditableTimerList";
import { timersData } from '../data/timers';
import ToggleableTimerForm from "./ToggleableTimerForm";
import { newTimer } from "../utils/helper";
import { useState } from "react";

export default function TimersDashboard() {
    const [timers, setTimers] = useState(timersData);

    const updateTimer = (attrs) => {
        setTimers((prevTimers) =>
            prevTimers.map((timer) =>
                timer.id === attrs.id ? { ...timer, title: attrs.title, ptoject: attrs.project } : timer
            )
        );
    };

    const handleCreateFormSubmit = (timer) => {
        createTimer(timer);
    };
 
    const handleEditFormSubmit = (attrs)=>{
        updateTimer(attrs);
    };

    const createTimer = (timer) => {
        const t = newTimer(timer);
        setTimers((prevTimers)=>[...prevTimers,t]);
    };

    
    return (
        <div className="text-center">
            <div className="flex flex-col">
                <EditableTimerList timers={timers} onFormSubmit={handleEditFormSubmit} />
                <ToggleableTimerForm onFormSubmit={handleCreateFormSubmit} />
            </div>
        </div>
    );
}