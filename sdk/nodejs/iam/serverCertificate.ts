// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IAM::ServerCertificate
 */
export class ServerCertificate extends pulumi.CustomResource {
    /**
     * Get an existing ServerCertificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ServerCertificate {
        return new ServerCertificate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iam:ServerCertificate';

    /**
     * Returns true if the given object is an instance of ServerCertificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ServerCertificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ServerCertificate.__pulumiType;
    }

    /**
     * Amazon Resource Name (ARN) of the server certificate
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly certificateBody!: pulumi.Output<string | undefined>;
    public readonly certificateChain!: pulumi.Output<string | undefined>;
    public readonly path!: pulumi.Output<string | undefined>;
    public readonly privateKey!: pulumi.Output<string | undefined>;
    public readonly serverCertificateName!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.iam.ServerCertificateTag[] | undefined>;

    /**
     * Create a ServerCertificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ServerCertificateArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["certificateBody"] = args ? args.certificateBody : undefined;
            resourceInputs["certificateChain"] = args ? args.certificateChain : undefined;
            resourceInputs["path"] = args ? args.path : undefined;
            resourceInputs["privateKey"] = args ? args.privateKey : undefined;
            resourceInputs["serverCertificateName"] = args ? args.serverCertificateName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["certificateBody"] = undefined /*out*/;
            resourceInputs["certificateChain"] = undefined /*out*/;
            resourceInputs["path"] = undefined /*out*/;
            resourceInputs["privateKey"] = undefined /*out*/;
            resourceInputs["serverCertificateName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["certificateBody", "certificateChain", "privateKey", "serverCertificateName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ServerCertificate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ServerCertificate resource.
 */
export interface ServerCertificateArgs {
    certificateBody?: pulumi.Input<string>;
    certificateChain?: pulumi.Input<string>;
    path?: pulumi.Input<string>;
    privateKey?: pulumi.Input<string>;
    serverCertificateName?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.iam.ServerCertificateTagArgs>[]>;
}
