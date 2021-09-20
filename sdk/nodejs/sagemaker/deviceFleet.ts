// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::SageMaker::DeviceFleet
 */
export class DeviceFleet extends pulumi.CustomResource {
    /**
     * Get an existing DeviceFleet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DeviceFleet {
        return new DeviceFleet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:sagemaker:DeviceFleet';

    /**
     * Returns true if the given object is an instance of DeviceFleet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DeviceFleet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DeviceFleet.__pulumiType;
    }

    /**
     * Description for the edge device fleet
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the edge device fleet
     */
    public readonly deviceFleetName!: pulumi.Output<string>;
    /**
     * S3 bucket and an ecryption key id (if available) to store outputs for the fleet
     */
    public readonly outputConfig!: pulumi.Output<outputs.sagemaker.DeviceFleetEdgeOutputConfig>;
    /**
     * Role associated with the device fleet
     */
    public readonly roleArn!: pulumi.Output<string>;
    /**
     * Associate tags with the resource
     */
    public readonly tags!: pulumi.Output<outputs.sagemaker.DeviceFleetTag[] | undefined>;

    /**
     * Create a DeviceFleet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DeviceFleetArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.deviceFleetName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'deviceFleetName'");
            }
            if ((!args || args.outputConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'outputConfig'");
            }
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["deviceFleetName"] = args ? args.deviceFleetName : undefined;
            inputs["outputConfig"] = args ? args.outputConfig : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        } else {
            inputs["description"] = undefined /*out*/;
            inputs["deviceFleetName"] = undefined /*out*/;
            inputs["outputConfig"] = undefined /*out*/;
            inputs["roleArn"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(DeviceFleet.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a DeviceFleet resource.
 */
export interface DeviceFleetArgs {
    /**
     * Description for the edge device fleet
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the edge device fleet
     */
    deviceFleetName: pulumi.Input<string>;
    /**
     * S3 bucket and an ecryption key id (if available) to store outputs for the fleet
     */
    outputConfig: pulumi.Input<inputs.sagemaker.DeviceFleetEdgeOutputConfigArgs>;
    /**
     * Role associated with the device fleet
     */
    roleArn: pulumi.Input<string>;
    /**
     * Associate tags with the resource
     */
    tags?: pulumi.Input<pulumi.Input<inputs.sagemaker.DeviceFleetTagArgs>[]>;
}
