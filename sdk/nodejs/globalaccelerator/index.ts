// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./accelerator";
export * from "./endpointGroup";
export * from "./listener";

// Import resources to register:
import { Accelerator } from "./accelerator";
import { EndpointGroup } from "./endpointGroup";
import { Listener } from "./listener";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "cloudformation:GlobalAccelerator:Accelerator":
                return new Accelerator(name, <any>undefined, { urn })
            case "cloudformation:GlobalAccelerator:EndpointGroup":
                return new EndpointGroup(name, <any>undefined, { urn })
            case "cloudformation:GlobalAccelerator:Listener":
                return new Listener(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("cloudformation", "GlobalAccelerator", _module)