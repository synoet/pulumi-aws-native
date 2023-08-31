// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Use the AWS::IoT::Certificate resource to declare an AWS IoT X.509 certificate.
 */
export class Certificate extends pulumi.CustomResource {
    /**
     * Get an existing Certificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Certificate {
        return new Certificate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iot:Certificate';

    /**
     * Returns true if the given object is an instance of Certificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Certificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Certificate.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly caCertificatePem!: pulumi.Output<string | undefined>;
    public readonly certificateMode!: pulumi.Output<enums.iot.CertificateMode | undefined>;
    public readonly certificatePem!: pulumi.Output<string | undefined>;
    public readonly certificateSigningRequest!: pulumi.Output<string | undefined>;
    public readonly status!: pulumi.Output<enums.iot.CertificateStatus>;

    /**
     * Create a Certificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CertificateArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.status === undefined) && !opts.urn) {
                throw new Error("Missing required property 'status'");
            }
            resourceInputs["caCertificatePem"] = args ? args.caCertificatePem : undefined;
            resourceInputs["certificateMode"] = args ? args.certificateMode : undefined;
            resourceInputs["certificatePem"] = args ? args.certificatePem : undefined;
            resourceInputs["certificateSigningRequest"] = args ? args.certificateSigningRequest : undefined;
            resourceInputs["status"] = args ? args.status : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["caCertificatePem"] = undefined /*out*/;
            resourceInputs["certificateMode"] = undefined /*out*/;
            resourceInputs["certificatePem"] = undefined /*out*/;
            resourceInputs["certificateSigningRequest"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["caCertificatePem", "certificateMode", "certificatePem", "certificateSigningRequest"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Certificate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Certificate resource.
 */
export interface CertificateArgs {
    caCertificatePem?: pulumi.Input<string>;
    certificateMode?: pulumi.Input<enums.iot.CertificateMode>;
    certificatePem?: pulumi.Input<string>;
    certificateSigningRequest?: pulumi.Input<string>;
    status: pulumi.Input<enums.iot.CertificateStatus>;
}
