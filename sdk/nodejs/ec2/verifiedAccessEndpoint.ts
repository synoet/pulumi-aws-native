// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::EC2::VerifiedAccessEndpoint resource creates an AWS EC2 Verified Access Endpoint.
 */
export class VerifiedAccessEndpoint extends pulumi.CustomResource {
    /**
     * Get an existing VerifiedAccessEndpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VerifiedAccessEndpoint {
        return new VerifiedAccessEndpoint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VerifiedAccessEndpoint';

    /**
     * Returns true if the given object is an instance of VerifiedAccessEndpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VerifiedAccessEndpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VerifiedAccessEndpoint.__pulumiType;
    }

    /**
     * The DNS name for users to reach your application.
     */
    public readonly applicationDomain!: pulumi.Output<string>;
    /**
     * The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.
     */
    public readonly attachmentType!: pulumi.Output<string>;
    /**
     * The creation time.
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * A description for the AWS Verified Access endpoint.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Returned if endpoint has a device trust provider attached.
     */
    public /*out*/ readonly deviceValidationDomain!: pulumi.Output<string>;
    /**
     * The ARN of a public TLS/SSL certificate imported into or created with ACM.
     */
    public readonly domainCertificateArn!: pulumi.Output<string>;
    /**
     * A DNS name that is generated for the endpoint.
     */
    public /*out*/ readonly endpointDomain!: pulumi.Output<string>;
    /**
     * A custom identifier that gets prepended to a DNS name that is generated for the endpoint.
     */
    public readonly endpointDomainPrefix!: pulumi.Output<string>;
    /**
     * The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.
     */
    public readonly endpointType!: pulumi.Output<string>;
    /**
     * The last updated time.
     */
    public /*out*/ readonly lastUpdatedTime!: pulumi.Output<string>;
    /**
     * The load balancer details if creating the AWS Verified Access endpoint as load-balancer type.
     */
    public readonly loadBalancerOptions!: pulumi.Output<outputs.ec2.VerifiedAccessEndpointLoadBalancerOptions | undefined>;
    /**
     * The options for network-interface type endpoint.
     */
    public readonly networkInterfaceOptions!: pulumi.Output<outputs.ec2.VerifiedAccessEndpointNetworkInterfaceOptions | undefined>;
    /**
     * The AWS Verified Access policy document.
     */
    public readonly policyDocument!: pulumi.Output<string | undefined>;
    /**
     * The status of the Verified Access policy.
     */
    public readonly policyEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The IDs of the security groups for the endpoint.
     */
    public readonly securityGroupIds!: pulumi.Output<string[] | undefined>;
    /**
     * The endpoint status.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.VerifiedAccessEndpointTag[] | undefined>;
    /**
     * The ID of the AWS Verified Access endpoint.
     */
    public /*out*/ readonly verifiedAccessEndpointId!: pulumi.Output<string>;
    /**
     * The ID of the AWS Verified Access group.
     */
    public readonly verifiedAccessGroupId!: pulumi.Output<string>;
    /**
     * The ID of the AWS Verified Access instance.
     */
    public /*out*/ readonly verifiedAccessInstanceId!: pulumi.Output<string>;

    /**
     * Create a VerifiedAccessEndpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VerifiedAccessEndpointArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.applicationDomain === undefined) && !opts.urn) {
                throw new Error("Missing required property 'applicationDomain'");
            }
            if ((!args || args.attachmentType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'attachmentType'");
            }
            if ((!args || args.domainCertificateArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domainCertificateArn'");
            }
            if ((!args || args.endpointDomainPrefix === undefined) && !opts.urn) {
                throw new Error("Missing required property 'endpointDomainPrefix'");
            }
            if ((!args || args.endpointType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'endpointType'");
            }
            if ((!args || args.verifiedAccessGroupId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'verifiedAccessGroupId'");
            }
            resourceInputs["applicationDomain"] = args ? args.applicationDomain : undefined;
            resourceInputs["attachmentType"] = args ? args.attachmentType : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["domainCertificateArn"] = args ? args.domainCertificateArn : undefined;
            resourceInputs["endpointDomainPrefix"] = args ? args.endpointDomainPrefix : undefined;
            resourceInputs["endpointType"] = args ? args.endpointType : undefined;
            resourceInputs["loadBalancerOptions"] = args ? args.loadBalancerOptions : undefined;
            resourceInputs["networkInterfaceOptions"] = args ? args.networkInterfaceOptions : undefined;
            resourceInputs["policyDocument"] = args ? args.policyDocument : undefined;
            resourceInputs["policyEnabled"] = args ? args.policyEnabled : undefined;
            resourceInputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["verifiedAccessGroupId"] = args ? args.verifiedAccessGroupId : undefined;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["deviceValidationDomain"] = undefined /*out*/;
            resourceInputs["endpointDomain"] = undefined /*out*/;
            resourceInputs["lastUpdatedTime"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["verifiedAccessEndpointId"] = undefined /*out*/;
            resourceInputs["verifiedAccessInstanceId"] = undefined /*out*/;
        } else {
            resourceInputs["applicationDomain"] = undefined /*out*/;
            resourceInputs["attachmentType"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["deviceValidationDomain"] = undefined /*out*/;
            resourceInputs["domainCertificateArn"] = undefined /*out*/;
            resourceInputs["endpointDomain"] = undefined /*out*/;
            resourceInputs["endpointDomainPrefix"] = undefined /*out*/;
            resourceInputs["endpointType"] = undefined /*out*/;
            resourceInputs["lastUpdatedTime"] = undefined /*out*/;
            resourceInputs["loadBalancerOptions"] = undefined /*out*/;
            resourceInputs["networkInterfaceOptions"] = undefined /*out*/;
            resourceInputs["policyDocument"] = undefined /*out*/;
            resourceInputs["policyEnabled"] = undefined /*out*/;
            resourceInputs["securityGroupIds"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["verifiedAccessEndpointId"] = undefined /*out*/;
            resourceInputs["verifiedAccessGroupId"] = undefined /*out*/;
            resourceInputs["verifiedAccessInstanceId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(VerifiedAccessEndpoint.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VerifiedAccessEndpoint resource.
 */
export interface VerifiedAccessEndpointArgs {
    /**
     * The DNS name for users to reach your application.
     */
    applicationDomain: pulumi.Input<string>;
    /**
     * The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.
     */
    attachmentType: pulumi.Input<string>;
    /**
     * A description for the AWS Verified Access endpoint.
     */
    description?: pulumi.Input<string>;
    /**
     * The ARN of a public TLS/SSL certificate imported into or created with ACM.
     */
    domainCertificateArn: pulumi.Input<string>;
    /**
     * A custom identifier that gets prepended to a DNS name that is generated for the endpoint.
     */
    endpointDomainPrefix: pulumi.Input<string>;
    /**
     * The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.
     */
    endpointType: pulumi.Input<string>;
    /**
     * The load balancer details if creating the AWS Verified Access endpoint as load-balancer type.
     */
    loadBalancerOptions?: pulumi.Input<inputs.ec2.VerifiedAccessEndpointLoadBalancerOptionsArgs>;
    /**
     * The options for network-interface type endpoint.
     */
    networkInterfaceOptions?: pulumi.Input<inputs.ec2.VerifiedAccessEndpointNetworkInterfaceOptionsArgs>;
    /**
     * The AWS Verified Access policy document.
     */
    policyDocument?: pulumi.Input<string>;
    /**
     * The status of the Verified Access policy.
     */
    policyEnabled?: pulumi.Input<boolean>;
    /**
     * The IDs of the security groups for the endpoint.
     */
    securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.VerifiedAccessEndpointTagArgs>[]>;
    /**
     * The ID of the AWS Verified Access group.
     */
    verifiedAccessGroupId: pulumi.Input<string>;
}
