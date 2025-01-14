// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { DeliveryStreamArgs } from "./deliveryStream";
export type DeliveryStream = import("./deliveryStream").DeliveryStream;
export const DeliveryStream: typeof import("./deliveryStream").DeliveryStream = null as any;
utilities.lazyLoad(exports, ["DeliveryStream"], () => require("./deliveryStream"));

export { GetDeliveryStreamArgs, GetDeliveryStreamResult, GetDeliveryStreamOutputArgs } from "./getDeliveryStream";
export const getDeliveryStream: typeof import("./getDeliveryStream").getDeliveryStream = null as any;
export const getDeliveryStreamOutput: typeof import("./getDeliveryStream").getDeliveryStreamOutput = null as any;
utilities.lazyLoad(exports, ["getDeliveryStream","getDeliveryStreamOutput"], () => require("./getDeliveryStream"));


// Export enums:
export * from "../types/enums/kinesisfirehose";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:kinesisfirehose:DeliveryStream":
                return new DeliveryStream(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "kinesisfirehose", _module)
