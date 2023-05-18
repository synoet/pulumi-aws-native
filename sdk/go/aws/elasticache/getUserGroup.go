// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package elasticache

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ElastiCache::UserGroup
func LookupUserGroup(ctx *pulumi.Context, args *LookupUserGroupArgs, opts ...pulumi.InvokeOption) (*LookupUserGroupResult, error) {
	var rv LookupUserGroupResult
	err := ctx.Invoke("aws-native:elasticache:getUserGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupUserGroupArgs struct {
	// The ID of the user group.
	UserGroupId string `pulumi:"userGroupId"`
}

type LookupUserGroupResult struct {
	// The Amazon Resource Name (ARN) of the user account.
	Arn *string `pulumi:"arn"`
	// Indicates user group status. Can be "creating", "active", "modifying", "deleting".
	Status *string `pulumi:"status"`
	// An array of key-value pairs to apply to this user.
	Tags []UserGroupTag `pulumi:"tags"`
	// List of users associated to this user group.
	UserIds []string `pulumi:"userIds"`
}

func LookupUserGroupOutput(ctx *pulumi.Context, args LookupUserGroupOutputArgs, opts ...pulumi.InvokeOption) LookupUserGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupUserGroupResult, error) {
			args := v.(LookupUserGroupArgs)
			r, err := LookupUserGroup(ctx, &args, opts...)
			var s LookupUserGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupUserGroupResultOutput)
}

type LookupUserGroupOutputArgs struct {
	// The ID of the user group.
	UserGroupId pulumi.StringInput `pulumi:"userGroupId"`
}

func (LookupUserGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserGroupArgs)(nil)).Elem()
}

type LookupUserGroupResultOutput struct{ *pulumi.OutputState }

func (LookupUserGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserGroupResult)(nil)).Elem()
}

func (o LookupUserGroupResultOutput) ToLookupUserGroupResultOutput() LookupUserGroupResultOutput {
	return o
}

func (o LookupUserGroupResultOutput) ToLookupUserGroupResultOutputWithContext(ctx context.Context) LookupUserGroupResultOutput {
	return o
}

// The Amazon Resource Name (ARN) of the user account.
func (o LookupUserGroupResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserGroupResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Indicates user group status. Can be "creating", "active", "modifying", "deleting".
func (o LookupUserGroupResultOutput) Status() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserGroupResult) *string { return v.Status }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this user.
func (o LookupUserGroupResultOutput) Tags() UserGroupTagArrayOutput {
	return o.ApplyT(func(v LookupUserGroupResult) []UserGroupTag { return v.Tags }).(UserGroupTagArrayOutput)
}

// List of users associated to this user group.
func (o LookupUserGroupResultOutput) UserIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupUserGroupResult) []string { return v.UserIds }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupUserGroupResultOutput{})
}
