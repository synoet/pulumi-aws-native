// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Lightsail::Instance
 */
export class Instance extends pulumi.CustomResource {
    /**
     * Get an existing Instance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Instance {
        return new Instance(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lightsail:Instance';

    /**
     * Returns true if the given object is an instance of Instance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Instance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Instance.__pulumiType;
    }

    /**
     * An array of objects representing the add-ons to enable for the new instance.
     */
    public readonly addOns!: pulumi.Output<outputs.lightsail.InstanceAddOn[] | undefined>;
    /**
     * The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
     */
    public readonly availabilityZone!: pulumi.Output<string | undefined>;
    /**
     * The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
     */
    public readonly blueprintId!: pulumi.Output<string>;
    /**
     * The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
     */
    public readonly bundleId!: pulumi.Output<string>;
    public readonly hardware!: pulumi.Output<outputs.lightsail.InstanceHardware | undefined>;
    public /*out*/ readonly instanceArn!: pulumi.Output<string>;
    /**
     * The names to use for your new Lightsail instance.
     */
    public readonly instanceName!: pulumi.Output<string>;
    /**
     * Is the IP Address of the Instance is the static IP
     */
    public /*out*/ readonly isStaticIp!: pulumi.Output<boolean>;
    /**
     * The name of your key pair.
     */
    public readonly keyPairName!: pulumi.Output<string | undefined>;
    public readonly location!: pulumi.Output<outputs.lightsail.InstanceLocation | undefined>;
    public readonly networking!: pulumi.Output<outputs.lightsail.InstanceNetworking | undefined>;
    /**
     * Private IP Address of the Instance
     */
    public /*out*/ readonly privateIpAddress!: pulumi.Output<string>;
    /**
     * Public IP Address of the Instance
     */
    public /*out*/ readonly publicIpAddress!: pulumi.Output<string>;
    /**
     * Resource type of Lightsail instance.
     */
    public /*out*/ readonly resourceType!: pulumi.Output<string>;
    /**
     * SSH Key Name of the  Lightsail instance.
     */
    public /*out*/ readonly sshKeyName!: pulumi.Output<string>;
    public readonly state!: pulumi.Output<outputs.lightsail.InstanceState | undefined>;
    /**
     * Support code to help identify any issues
     */
    public /*out*/ readonly supportCode!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.lightsail.InstanceTag[] | undefined>;
    /**
     * A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
     */
    public readonly userData!: pulumi.Output<string | undefined>;
    /**
     * Username of the  Lightsail instance.
     */
    public /*out*/ readonly userName!: pulumi.Output<string>;

    /**
     * Create a Instance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.blueprintId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'blueprintId'");
            }
            if ((!args || args.bundleId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bundleId'");
            }
            if ((!args || args.instanceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceName'");
            }
            inputs["addOns"] = args ? args.addOns : undefined;
            inputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            inputs["blueprintId"] = args ? args.blueprintId : undefined;
            inputs["bundleId"] = args ? args.bundleId : undefined;
            inputs["hardware"] = args ? args.hardware : undefined;
            inputs["instanceName"] = args ? args.instanceName : undefined;
            inputs["keyPairName"] = args ? args.keyPairName : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["networking"] = args ? args.networking : undefined;
            inputs["state"] = args ? args.state : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["userData"] = args ? args.userData : undefined;
            inputs["instanceArn"] = undefined /*out*/;
            inputs["isStaticIp"] = undefined /*out*/;
            inputs["privateIpAddress"] = undefined /*out*/;
            inputs["publicIpAddress"] = undefined /*out*/;
            inputs["resourceType"] = undefined /*out*/;
            inputs["sshKeyName"] = undefined /*out*/;
            inputs["supportCode"] = undefined /*out*/;
            inputs["userName"] = undefined /*out*/;
        } else {
            inputs["addOns"] = undefined /*out*/;
            inputs["availabilityZone"] = undefined /*out*/;
            inputs["blueprintId"] = undefined /*out*/;
            inputs["bundleId"] = undefined /*out*/;
            inputs["hardware"] = undefined /*out*/;
            inputs["instanceArn"] = undefined /*out*/;
            inputs["instanceName"] = undefined /*out*/;
            inputs["isStaticIp"] = undefined /*out*/;
            inputs["keyPairName"] = undefined /*out*/;
            inputs["location"] = undefined /*out*/;
            inputs["networking"] = undefined /*out*/;
            inputs["privateIpAddress"] = undefined /*out*/;
            inputs["publicIpAddress"] = undefined /*out*/;
            inputs["resourceType"] = undefined /*out*/;
            inputs["sshKeyName"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["supportCode"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["userData"] = undefined /*out*/;
            inputs["userName"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Instance.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Instance resource.
 */
export interface InstanceArgs {
    /**
     * An array of objects representing the add-ons to enable for the new instance.
     */
    addOns?: pulumi.Input<pulumi.Input<inputs.lightsail.InstanceAddOnArgs>[]>;
    /**
     * The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
     */
    blueprintId: pulumi.Input<string>;
    /**
     * The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
     */
    bundleId: pulumi.Input<string>;
    hardware?: pulumi.Input<inputs.lightsail.InstanceHardwareArgs>;
    /**
     * The names to use for your new Lightsail instance.
     */
    instanceName: pulumi.Input<string>;
    /**
     * The name of your key pair.
     */
    keyPairName?: pulumi.Input<string>;
    location?: pulumi.Input<inputs.lightsail.InstanceLocationArgs>;
    networking?: pulumi.Input<inputs.lightsail.InstanceNetworkingArgs>;
    state?: pulumi.Input<inputs.lightsail.InstanceStateArgs>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.lightsail.InstanceTagArgs>[]>;
    /**
     * A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
     */
    userData?: pulumi.Input<string>;
}
