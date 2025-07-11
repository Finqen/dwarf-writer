use crate::InputFile;
use crate::Opt;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

impl InputFile for CalleeInput {}

impl CalleeInput {
    pub fn data(&self, _cfg: &Opt) -> CalleeData {
        CalleeData {
            callees: self.callees.clone(),
        }
    }
}

pub struct CalleeData {
    pub callees: HashMap<String, CalleeInfo>,
}

/// Represents a single callee input file with function call information.
#[derive(Serialize, Deserialize, Debug)]
pub struct CalleeInput {
    #[serde(flatten)]
    callees: HashMap<String, CalleeInfo>,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct CalleeInfo {
    pub definition: u64,
    pub calls: Vec<u64>,
}
