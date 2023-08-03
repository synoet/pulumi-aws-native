// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::NetworkManager::Device type describes a device.
 */
export class Device extends pulumi.CustomResource {
    /**
     * Get an existing Device resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Device {
        return new Device(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:networkmanager:Device';

    /**
     * Returns true if the given object is an instance of Device.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Device {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Device.__pulumiType;
    }

    /**
     * The Amazon Web Services location of the device, if applicable.
     */
    public readonly awsLocation!: pulumi.Output<outputs.networkmanager.DeviceAwsLocation | undefined>;
    /**
     * The date and time that the device was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The description of the device.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the device.
     */
    public /*out*/ readonly deviceArn!: pulumi.Output<string>;
    /**
     * The ID of the device.
     */
    public /*out*/ readonly deviceId!: pulumi.Output<string>;
    /**
     * The ID of the global network.
     */
    public readonly globalNetworkId!: pulumi.Output<string>;
    /**
     * The site location.
     */
    public readonly location!: pulumi.Output<outputs.networkmanager.DeviceLocation | undefined>;
    /**
     * The device model
     */
    public readonly model!: pulumi.Output<string | undefined>;
    /**
     * The device serial number.
     */
    public readonly serialNumber!: pulumi.Output<string | undefined>;
    /**
     * The site ID.
     */
    public readonly siteId!: pulumi.Output<string | undefined>;
    /**
     * The tags for the device.
     */
    public readonly tags!: pulumi.Output<outputs.networkmanager.DeviceTag[] | undefined>;
    /**
     * The device type.
     */
    public readonly type!: pulumi.Output<string | undefined>;
    /**
     * The device vendor.
     */
    public readonly vendor!: pulumi.Output<string | undefined>;

    /**
     * Create a Device resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DeviceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.globalNetworkId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'globalNetworkId'");
            }
            resourceInputs["awsLocation"] = args ? args.awsLocation : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["globalNetworkId"] = args ? args.globalNetworkId : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["model"] = args ? args.model : undefined;
            resourceInputs["serialNumber"] = args ? args.serialNumber : undefined;
            resourceInputs["siteId"] = args ? args.siteId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["vendor"] = args ? args.vendor : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["deviceArn"] = undefined /*out*/;
            resourceInputs["deviceId"] = undefined /*out*/;
        } else {
            resourceInputs["awsLocation"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["deviceArn"] = undefined /*out*/;
            resourceInputs["deviceId"] = undefined /*out*/;
            resourceInputs["globalNetworkId"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["model"] = undefined /*out*/;
            resourceInputs["serialNumber"] = undefined /*out*/;
            resourceInputs["siteId"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["vendor"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Device.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Device resource.
 */
export interface DeviceArgs {
    /**
     * The Amazon Web Services location of the device, if applicable.
     */
    awsLocation?: pulumi.Input<inputs.networkmanager.DeviceAwsLocationArgs>;
    /**
     * The description of the device.
     */
    description?: pulumi.Input<string>;
    /**
     * The ID of the global network.
     */
    globalNetworkId: pulumi.Input<string>;
    /**
     * The site location.
     */
    location?: pulumi.Input<inputs.networkmanager.DeviceLocationArgs>;
    /**
     * The device model
     */
    model?: pulumi.Input<string>;
    /**
     * The device serial number.
     */
    serialNumber?: pulumi.Input<string>;
    /**
     * The site ID.
     */
    siteId?: pulumi.Input<string>;
    /**
     * The tags for the device.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.networkmanager.DeviceTagArgs>[]>;
    /**
     * The device type.
     */
    type?: pulumi.Input<string>;
    /**
     * The device vendor.
     */
    vendor?: pulumi.Input<string>;
}
