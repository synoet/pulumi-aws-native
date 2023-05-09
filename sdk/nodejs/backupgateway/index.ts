// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetHypervisorArgs, GetHypervisorResult, GetHypervisorOutputArgs } from "./getHypervisor";
export const getHypervisor: typeof import("./getHypervisor").getHypervisor = null as any;
export const getHypervisorOutput: typeof import("./getHypervisor").getHypervisorOutput = null as any;
utilities.lazyLoad(exports, ["getHypervisor","getHypervisorOutput"], () => require("./getHypervisor"));

export { HypervisorArgs } from "./hypervisor";
export type Hypervisor = import("./hypervisor").Hypervisor;
export const Hypervisor: typeof import("./hypervisor").Hypervisor = null as any;
utilities.lazyLoad(exports, ["Hypervisor"], () => require("./hypervisor"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:backupgateway:Hypervisor":
                return new Hypervisor(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "backupgateway", _module)
