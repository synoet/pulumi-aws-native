// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetObservabilityConfigurationArgs, GetObservabilityConfigurationResult, GetObservabilityConfigurationOutputArgs } from "./getObservabilityConfiguration";
export const getObservabilityConfiguration: typeof import("./getObservabilityConfiguration").getObservabilityConfiguration = null as any;
export const getObservabilityConfigurationOutput: typeof import("./getObservabilityConfiguration").getObservabilityConfigurationOutput = null as any;
utilities.lazyLoad(exports, ["getObservabilityConfiguration","getObservabilityConfigurationOutput"], () => require("./getObservabilityConfiguration"));

export { GetServiceArgs, GetServiceResult, GetServiceOutputArgs } from "./getService";
export const getService: typeof import("./getService").getService = null as any;
export const getServiceOutput: typeof import("./getService").getServiceOutput = null as any;
utilities.lazyLoad(exports, ["getService","getServiceOutput"], () => require("./getService"));

export { GetVpcConnectorArgs, GetVpcConnectorResult, GetVpcConnectorOutputArgs } from "./getVpcConnector";
export const getVpcConnector: typeof import("./getVpcConnector").getVpcConnector = null as any;
export const getVpcConnectorOutput: typeof import("./getVpcConnector").getVpcConnectorOutput = null as any;
utilities.lazyLoad(exports, ["getVpcConnector","getVpcConnectorOutput"], () => require("./getVpcConnector"));

export { ObservabilityConfigurationArgs } from "./observabilityConfiguration";
export type ObservabilityConfiguration = import("./observabilityConfiguration").ObservabilityConfiguration;
export const ObservabilityConfiguration: typeof import("./observabilityConfiguration").ObservabilityConfiguration = null as any;
utilities.lazyLoad(exports, ["ObservabilityConfiguration"], () => require("./observabilityConfiguration"));

export { ServiceArgs } from "./service";
export type Service = import("./service").Service;
export const Service: typeof import("./service").Service = null as any;
utilities.lazyLoad(exports, ["Service"], () => require("./service"));

export { VpcConnectorArgs } from "./vpcConnector";
export type VpcConnector = import("./vpcConnector").VpcConnector;
export const VpcConnector: typeof import("./vpcConnector").VpcConnector = null as any;
utilities.lazyLoad(exports, ["VpcConnector"], () => require("./vpcConnector"));


// Export enums:
export * from "../types/enums/apprunner";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:apprunner:ObservabilityConfiguration":
                return new ObservabilityConfiguration(name, <any>undefined, { urn })
            case "aws-native:apprunner:Service":
                return new Service(name, <any>undefined, { urn })
            case "aws-native:apprunner:VpcConnector":
                return new VpcConnector(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "apprunner", _module)
