// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::NetworkInterfacePermission
 *
 * @deprecated NetworkInterfacePermission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class NetworkInterfacePermission extends pulumi.CustomResource {
    /**
     * Get an existing NetworkInterfacePermission resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): NetworkInterfacePermission {
        pulumi.log.warn("NetworkInterfacePermission is deprecated: NetworkInterfacePermission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new NetworkInterfacePermission(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:NetworkInterfacePermission';

    /**
     * Returns true if the given object is an instance of NetworkInterfacePermission.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NetworkInterfacePermission {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NetworkInterfacePermission.__pulumiType;
    }

    public readonly awsAccountId!: pulumi.Output<string>;
    public readonly networkInterfaceId!: pulumi.Output<string>;
    public readonly permission!: pulumi.Output<string>;

    /**
     * Create a NetworkInterfacePermission resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated NetworkInterfacePermission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: NetworkInterfacePermissionArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("NetworkInterfacePermission is deprecated: NetworkInterfacePermission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.awsAccountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'awsAccountId'");
            }
            if ((!args || args.networkInterfaceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'networkInterfaceId'");
            }
            if ((!args || args.permission === undefined) && !opts.urn) {
                throw new Error("Missing required property 'permission'");
            }
            resourceInputs["awsAccountId"] = args ? args.awsAccountId : undefined;
            resourceInputs["networkInterfaceId"] = args ? args.networkInterfaceId : undefined;
            resourceInputs["permission"] = args ? args.permission : undefined;
        } else {
            resourceInputs["awsAccountId"] = undefined /*out*/;
            resourceInputs["networkInterfaceId"] = undefined /*out*/;
            resourceInputs["permission"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(NetworkInterfacePermission.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a NetworkInterfacePermission resource.
 */
export interface NetworkInterfacePermissionArgs {
    awsAccountId: pulumi.Input<string>;
    networkInterfaceId: pulumi.Input<string>;
    permission: pulumi.Input<string>;
}
